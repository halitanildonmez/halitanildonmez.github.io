---
layout: post
title: "Language flipcard part 2 - Creating a component at typescript"
date: 2021-11-10 20:53:00 -0000
categories: typescript javascript
---

Now it is time to create a front-end for this flip cards and for that I have chosen the Angular. Reason for this is because I want to learn the stuff a bit better and what better way to do it than to use for something I need. 

## Creating a Project

Angular has a really detailed tutorial [here](https://angular.io/tutorial/toh-pt1). So I followed that one but instead of creating a hero component, I have created a word component. 

## Displaying a List

Angular has a section on how to display a list with mock data initially. That is a good start for showing data. 

I generated a words component using `ng generate component words` and the name "words" is not a good name since I want to have a component with a single word in it. 

In any case that was mostly what I needed. All the code was auto generated and then I just had to test it. 

## Loading the Data

Since the data is json it is easy to load the data. It is json so it is easier to load and read. First step is to load the json data. 

Loading the data is possible with a simple import like this: `import SampleJson from '../html_converted.json';`

Now the "SimpleJson" object contains the key value pairs of the words. On loading the component I have done the following: 

{% highlight javascript %}
ngOnInit(): void {
	this.jsonObjectLength = Object.keys(SampleJson).length;
	this.objs = Object.entries(SampleJson);
}
createCounter(size:number) {
	this.words = [];
	for (let i = 0; i < size; i++) {
	  let rndNum:number = this.getRandomInt(0, this.jsonObjectLength);
	  var rndWord = this.objs[rndNum];
	  this.words.push({ id: rndNum, value_sv: rndWord[1][0], value_en: rndWord[1][1] });
	}
	return this.words;
}

onSelect(word: Word) {
	this.selectedWord = word;
}

getRandomInt(min:number, max:number) : number{
	min = Math.ceil(min);
	max = Math.floor(max);
	return Math.floor(Math.random() * (max - min + 1)) + min;
}
{% endhighlight %}

I am loading the data first. Then I am creating a random word component in the `createCounter` method. On select method is when a component is selected. The random selected word is then displayed. 

Random integer generation and getting a random word is done in the `getRandomInt` method. 

# Conclusion 

The final version looks like this: 

![My helpful screenshot](/finished.png)

If you hover over, you will see the English translation for each word.
