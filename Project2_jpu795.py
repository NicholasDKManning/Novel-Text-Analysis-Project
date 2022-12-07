#!/usr/bin/env python
# coding: utf-8

# In[275]:


# Nicholas Manning JPU795


# In[276]:


# Objective Include:

# Input a file
# Use String Manipulation
# Create String Tokens
# Use Loops and Dictionaries
# Print Tables of your Resulting Analysis


# In[277]:


# Introduction

# For this project, you'll write your own program from scratch where you pick one classic novel
# analyze it by:

# How many words
# How many unique words
# How often the most used words occur in the novel
# Priint out table of results
# Create Graph of Top 10 Most used words in the novel


# In[278]:


import os
import re


# In[279]:


# This cell will load the novel (Oliver Twist by Charles Dickens) into the 
# program and will be saved into a variable

path = r'C:\Users\nickm\Desktop\School\Programming for Data Science\olivertwist.txt'
    
assert os.path.isfile(path)

with open(path, 'r', encoding = 'utf8') as novel: # open the file path
    
    novel_txt = novel.read().lower() # read as a string and change all text to lower case
                                      
    updated_novel_txt = re.sub(r'[^a-z]', ' ', novel_txt).split() # get rid of special characters

    unique_words_in_novel = set(updated_novel_txt_with_space.split()) # sets will not include repeated words


# In[280]:


print(updated_novel_txt)

# This will show that updated_novel_txt only includes letters from the alphabet
# No special characters or numbers will be printed or included in the variable


# In[281]:


print(f'The number of words and unique words in Oliver Twist is {len(updated_novel_txt)} and {len(unique_words_in_novel)}.')

# This will show the number of words in the text without special characters
# This will also show the number of unique words also without special characters


# In[282]:


dictionary = dict() # create a dictionary

for line in updated_novel_txt: # for each line in the novel without special characters

    text = line.split(" ") # gets rid of white spaces

    for word in text: # each word in each line

        if word in dictionary: # if a new word is found

            dictionary[word] = dictionary[word] + 1 # add 1 to the value of the word
            
        else: # if a word does not have multiples set its value to 1

            dictionary[word] = 1

for key in list(dictionary.keys()): 


    print(key, ":", dictionary[key]) # prints the new dictionary


# In[283]:


dictionary = dict((x, y) for x, y in dictionary.items() if y >= 1875) # code to find the most occurring words in the dictionary

dictionary # call function


# In[284]:


import matplotlib.pylab as plt
import seaborn as sns
import pandas as pd

data = pd.DataFrame(dictionary.items(), columns = ['Top Ten Occurring Words', 'Amount Word Occurred'])

# ^ converting the dictionary into a data frame type

data

# ^ calls the dataframe

data.plot.bar(title = 'Top Ten Occurring Words in the Book: Oliver Twist by Charles Dickens', x = 'Top Ten Occurring Words', y = 'Amount Word Occurred', fontsize = 12, rot = 45, figsize = (10, 6), legend = False)

# ^ plots the data frame as a bar graph with customized parameters to make it neat

# I opted to get rid of the legend since the x axis it labeled. I believe the legend is redundant and therefore unnecessary!


# In[ ]:




