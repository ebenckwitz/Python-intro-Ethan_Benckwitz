#!/usr/bin/env python3
#Author: Ethan Benckwitz
#Date: 8/30/2020
#Class: Theory of Operating Systems
#Assignment 0: Python Intro
#This assignment reads a given text file and counts the total number of times each
#word is given in the file. We then print the occurences in alphabetical order in a new file.

import sys          # command line arguments
import re           # regular expression tools

textFileName = sys.argv[1]
outputFileName = sys.argv[2]
    

#open the input file and remove punctuation while storing it in numWords
inputFile = open(textFileName, "r")
numWords = dict()
for line in inputFile:
    line = line.lower()
    line = line.replace('-', " ")
    line = line.replace("'", " ")
    line = re.sub('[^\w\s]', '', line)
    words = line.split()
   
    #moving all words and their occurences into numWords
    for word in words:
        if word not in numWords:
            numWords[word] = 0
        numWords[word] += 1

#create an ouptut file and print out all words and their occurences'
outputFile = open(outputFileName, "w")
for key, count in sorted(numWords.items()):
    outputFile.write(str(key) + " " + str(count) + "\n")

#closing the files
inputFile.close()
outputFile.close()
