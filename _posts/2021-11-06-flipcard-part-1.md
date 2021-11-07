---
layout: post
title: "Language flipcard part 1 - Getting and Parsing data"
date: 2021-11-06 20:53:00 -0000
categories: perl language swedish flipcard learn
---

In order to learn a new language (Swedish) I wanted to force myself to lean new words. One of the effective ways to do so is to find the most common 1000 words in the language and memorize them. 

In order to help with that process, I have created a website that will show some flip cards since I have read that it helps with memorization process. 

This will be a series of posts. First I will talk about how I got the data. Second part will describe how to create the website and component using angular. Final part will show how to load the data and the final version of the site. 

## Getting the words

First thing is to find the most common words. I found this website (https://www.101languages.net/swedish/most-common-swedish-words/) and saved all the words in an html file. 

The file is a table in html form. I just viewed the source and saved the file as html. Here is what the file roughly looked like: 

{% highlight html %}
</tr><tr class="row-101 odd">
	<td class="column-1">100</td><td class="column-2">två 	<audio id="wp_mep_1" src="http://www.101languages.net/audio/common-words/swedish/tva.mp3" controls="controls" preload="none">
		
		
		
		
		
		
		
	</audio>
<script type="text/javascript">
jQuery(document).ready(function($) {
	$('#wp_mep_1').mediaelementplayer({
		m:1
		
		,features: ['playpause','current','progress','duration','volume','tracks','fullscreen']
		,audioWidth:250,audioHeight:30
	});
});
</script>
</td><td class="column-3">two</td>
</tr><tr class="row-102 even">
	<td class="column-1">101</td><td class="column-2">något</td><td class="column-3">slightly</td>
</tr>
{% endhighlight%}

It has some tags for playing an audio but it is pretty straight forward. Note the long empty space as well. 

# Parsing the Data

I wanted to learn perl for string processing so I used it. I wrote a script that will take this data and convert it to json. 
Here is what it looks like. Note that I am only showing a part of the file. See the gist [here](https://gist.github.com/halitanildonmez/64b07d0c68bd83097afff64eed6f8cec) for the full version. 

{% highlight perl linenos %}
while ( my $token = $p->get_token ) {
    next unless $token->is_text;
    my($tag, $attr, $attrseq, $rawtxt) = @{ $token };
    my $index = index ($token->as_is, "jQuery");
    my $token_text = $token->as_is;

    if ($index == -1 && $token_text !~ /^\s*$/) {
        if ($token_text =~ /(\d+)/) {
            $ids = int($token_text);
            $count = 0;
        } else {
            $trs[$count] = $token_text;
            $count++;
        }
    }
    if ($count == 2 && $ids != -1) {
        $translations{$ids} = [$trs[0], $trs[1]];
    }
}
{% endhighlight%}

I am using the [html toke parser](https://metacpan.org/dist/HTML-TokeParser-Simple) library for getting the tags. So that is why line 3 exists. I had to do lots of experimenting in the absence of an auto complete and my lack of knowledge about the language. 

What is going on with line 4 and the if statement ? I am finding and removing the audio tags and everything similar to it. I am also using regex to see if the line is a digit so I can create an id, text pairing. Note that we have an id, Swedish and English text so need to create a pair and push that to the json object. 

The assumption we are making is that we will encounter an id first then the English and Swedish texts. When we find them we are adding them to a map and then we are done.

# Converting to JSON

Before we start, we need the [JSON library for PERL](https://metacpan.org/pod/JSON). 

After going through the data we created a map that has id as key and an array of 2 with English and Swedish words as value. Now we need to simply create a JSON object and write them to a file. 

{% highlight perl linenos%}
my $json = JSON->new->allow_nonref;
open(FH, '>', 'html_converted.json') or die $!;
print FH $json->encode( \%translations );
close(FH);
{% endhighlight %}

After this step, we will have a file in the following format: 

{% highlight json %}
{
	....
	"656":[
		"val",
		"choice"
	],
	"850":[
		"människa",
		"human"
	],
	....
}
{% endhighlight %}

## Conclusion

Now we have a json file and this will make it easier to load it to a wide range of frameworks. Next step is to create the front end for this application. I will use Angular to do this and will keep it as simple as possible as I do not enjoy the bits and pieces of doing front end. 

If you want to see the full code, it is here: [https://gist.github.com/halitanildonmez/64b07d0c68bd83097afff64eed6f8cec](https://gist.github.com/halitanildonmez/64b07d0c68bd83097afff64eed6f8cec)