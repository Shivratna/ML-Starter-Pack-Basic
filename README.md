# Basic ML-Training for Starters :
Basic character probability based ML use for text generation and training for starters in Machine Learning.
I have broken down things into a simple way.
Lets say you learn words and sentences and store that in your mind. Now for making your own sentence you choose words from your past sentences. The same way we start this journey of machine leaning. The Test1 and Test2 contain sample paragraphs to teach your model.

# Steps to start this journey :
* Open Training.py ( This code will take input from you to train the mind.txt file )
* Now after running Training.py and copying text paragraoh from Test 1 or 2 close the program
* Check and open mind.txt file too see how the data looks.
* The data in Mind.txt file is just a dictionary with piece by piece iteration of words as key and probablity of the next the word as elements.
* Now open the IMPLEMENTATION.py and give it a starter word and using that the program will produce a paragraph.
 
# USED:
* JSON
* NUMPY
* REQUESTS(is required)
* Markov chain model based

# Training:
This code takes the text data and stores it as a dictionary with character (window defined) and uses MARKOV Chain model to generate probablity based results.
Uses JSON to save the dict. data to text file

# Implementation.py
This code uses the stored data (trained data set in mind) to generate outputs that are totally random.

# Mind.txt
This text file contains the trained data set
