Sixle
#### Video Demo:  https://www.youtube.com/watch?v=QbPRUtdY-oQ
#### Description: New york times wordle game, but with six 6 letter words.

For my cs50 final project, I created Sixle, a new york times style wordle game but with a twist- 
six letter words instead of five letter words. Using a maximum of six guesses,
the user must use various six letter words in hopes of guessing the correct six letter word.
The user will know how close their six letter word is to the final answer with hints
in the form of the letter tiles turning yellow, grey, or green.
Yellow means that the letter is in the correct word but isn't in the correct position of the user's word
green means that the letter is in the correct word and the user's word which contained the letter in that position is correct.
finally, grey means that the letter doesn't appear at all in the correct word
Lets say that the user enters the word "cranes" and the answer is "brains"
The first letter, c, will turn grey since c is not in the word brains at all.
The second letter, r, will turn green since r is in the word "brains" and in the correct position (the second position)
The third letter, a, will also turn green because of the same reasoning.
The fourth letter, n, will turn yellow because although n is in the word brains, it's not in the correct position (n is the 4th position in the word "cranes" but in the 5th position in the correct word "cranes")
The fifth letter, e, will turn grey since e is not in "brains" at all.
finally, the sixth letter, s, will turn green since s is in the correct position.

Although, this isn't as simple as it seems. Such as, what if a word contains multiple of the same letters such as beefed?
In this case, let's say that the user guesses something like "cleeve"
The first letter, c, will turn grey, for the reasons aformentioned.
The second letter, l, will also turn grey, for the reason aforementioned also.
The third letter, e, is where things get a little tricky though. It'll turn green, because one of the e's beefed contains is in the third position, and the e is also in the third position in cleeve.
The fourth letter, also e, will turn yellow because beefed doesn't contain any e's in the fourth position of the word.
v will turn grey, for the reasons aforementioned.
finally, e, will turn yellow the reasons aformentioned also.

but there's another scenario for this: what if the user guesses beebee?
you can apply the same logic for the first three e's but things get a bit tricky at the 6th e.
the 6th e will turn grey because beefed only contains three e's, while at the 4th e, there're already 4 e's which is past three.

There's also another scenario: what if the user guesses "abided"

Here is where things get VERY tricky.

you can apply the same logic for the first three letters, but at the 4th letter, d, it gets tricky. At first glance, the 4th d would turn yellow
because beefed doesn't contain a d at the 4th position, but does contain a d in the word.
But as we continue, to the 6th letter, d also, we can see that we made a mistake on the 4th letter. Wouldn't the 6th d turn green since beefed also contains a d at the 6th position? But then, the word would turn into: GREY, GREY, GREY, YELLOW, GREEN, GREEEN which would imply that there're two d's in the correct word which is obviously not true. Beefed only has one d.
Instead of doing this, lets go back to where we made the mistake, the 4th letter, d.
this d would actually turn grey, while the 6th d would stay green.
This shows that in Sixle, and nyt wordle too, color priorities matter.
green > yellow > grey.

Finally, if you successfully guess the correct word, Sixle will show a win screen for you, showing the amount of guesses you used, the result of the game, and the correct word.
On the other hand, if you don't guess the correct word within six tries, Sixle will show a lose screen for you.
Showing the same things.

Now, let's talk about error handling. If you fail to enter the correct amount of letters (6), and you press the enter key in an attempt to sumbit the word, Sixle will prompt you with an alert telling you that you need to enter a six lettter long word.
If you enter a word that's not found in the word database that Sixle uses, Sixle will prompt you to enter an alternative word.

Now, about the design choices.
Originally, I was going to use the word database from wordnet, but it contained too many words for my liking and it was generally hard to convert into an sql database. I then did some research, and found that I could use my computer system's word database used for autocomplete and the like. So I copied my system's word database, converted it into an sql database, deleted all words without 6 letters in them, and I finally had my sql database.