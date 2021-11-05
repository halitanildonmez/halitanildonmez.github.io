---
layout: post
title: "Generating Safe Password"
date: 2021-11-03 21:33:00 -0000
categories: password generator safe cryptography
---
I have generated a safe password generator with dice throwing method in python just now. I followed the steps [here](https://www.eff.org/dice/)

What I did was to look up the methods to see how one can do the generation 

Read the file
find how to generate crypto safe file
read and write file

# Reading the File

First I had to read the file. With python it is really simple: 

{% highlight python linenos %}
with open('word_list.txt') as f:
	for line in f:
		print(line)
{% endhighlight %}

This is the first step but not enough because we also need to understand the file. The file has the following format: 

`11141	absinthe`

As you can see, there is first a 5 digit number and then the corresponding word. Before going any further, we should create a dictionary and place the values to a dictionary. 

For that we should make sure that we are splitting the line from the middle.

## Understanding the File

Python can create a dictionary easy enough: 

{% highlight python linenos %}
eff_words = {}
eff_words[11111] = 'word' 
{% endhighlight %}

In order to do that however we need to process the string input a bit like this: 

{% highlight python linenos %}
a = line.strip().split('	')
eff_words[int(a[0])] = a[1]
{% endhighlight %}

Lets break down what is happenning here line by line 

1. We are splitting the string from the point where we have the `	` in the string. If you have `number word` you will have `[number, word]` You can replace it with `\t` if you want. I think it is faster to just copy and paste the output.
2. We are casting the number to an integer because it will be easier to search the map with numbers after random number generation and assigning the word to the key.

# Generating Random Numbers

Now it is time to generate a random number. Random number generation needed to be safe. There are many places to do so but I have chosen python because I have seen several posts and decided to follow this one [here](https://pynative.com/cryptographically-secure-random-data-in-python/). 
It states that `SystemRandom` can be used to generate safe random numbers. See this post [here to see what I mean by safe](https://en.wikipedia.org/wiki/Cryptographically-secure_pseudorandom_number_generator). Granted that I do not know and have to take the word of python to be sure that it is safe. 

One more caveat is that we need to generate numbers up till 6 because we are simulating a dice throw. To not get things more complicated I have simply generated 5 digits as string and concetaneted them together (because I am lazy and whatever works). So the code will look like following: 

{% highlight python linenos %}
def rand_dice_num():
	v = ''
	for i in range(5):
		v += str(system_random.randint(1, 6))
	return int(v)

pass_gen = ''
for i in range(5):
	r = rand_dice_num()	
	pass_gen += str(eff_words[r])
{% endhighlight %}

I have just added a function to generate one random number and repeated the process 5 times.

# Conclusion

Adding all things together I got the following result below. It is a very simple thing but it will be able to maybe generate hints for 
some long master passwords. 

Thank you for reading!

{% highlight python linenos %}
import os
import random

system_random = random.SystemRandom()
eff_words = {}

def rand_dice_num():
	v = ''
	for i in range(5):
		v += str(system_random.randint(1, 6))
	return int(v)

with open('eff_large_wordlist.txt') as f:
	for line in f:
		a = line.strip().split('\t')
		eff_words[int(a[0])] = a[1]

pass_gen = ''
for i in range(5):
	r = rand_dice_num()	
	pass_gen += str(eff_words[r])

print(pass_gen)
{% endhighlight %}
