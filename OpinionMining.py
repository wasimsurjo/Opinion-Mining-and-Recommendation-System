"""
Created on Tue Mar 10 10:07:33 2020

@author: Wasim
"""

############################# PART 1a ##################################

#######################    OPINION MINING   ##########################

import pandas as pd
import numpy as np
import nltk
import matplotlib.pyplot as plt
from collections import Counter 
from textblob import TextBlob
import csv



data=pd.read_csv("data.csv", usecols = [0])

data.dropna()


print("(Rows,Columns) ==>",data.shape)
print(list(data.columns.values))

#nltk.download()  
#This Process Must Be Executed If The Program Runs For The First Time

tagged_opinions = []    
#The Tokens Will Be Added Here After POS Tagging

for i in range(len(data)) : 
# print(data.iloc[i][0]) #The real opinion in original form
  text = nltk.word_tokenize(data.iloc[i][0]) #Tokenize the opinion
  tagged_opinions.append(nltk.pos_tag(text)) #Tag and add to tagged opinions list
 # print(nltk.pos_tag(text))    #Sample POS tagging

num=2 #Used as counter for Loops

print("Original Opinions\n")
print(data.iloc[num][0],"\n")
print("Tokens:\n")
print(nltk.word_tokenize(data.iloc[num][0]),"\n")
print("POS TAGGED TOKENS:\n")
print(tagged_opinions[0],"\n")


### Prepare The Grammar
results=[]
expr = "NP: {<DT|PP|CD>?<JJ||JJR|JJS>*<NN|NNS|PRP|NNP|IN|PRP\$>+<VBD|VBZ|VBN|VBP|IN>*<JJ|RB>*<PRP|NN|NNS>*}"
parser = nltk.RegexpParser(expr)

### Prepare a CSV File To Write Results
csvFile = open('result.csv', 'a')
csvWriter = csv.writer(csvFile)



# Parse the tagged opinions based on the grammar
for h in range(len(data)):
 results.append(parser.parse(tagged_opinions[h]))
# print(results[h])

# Extract the opinions
for z in range(len(data)):
   # print("Opinion: ")
    csvWriter.writerow('Opinion')
    for result in results[z]:
     if type(result) == nltk.tree.Tree:
         assoc=[]
         for res in result:
             assoc.append(res[0])
         if len(assoc) > 1:
             #print("Written")
             csvWriter.writerow(assoc)
        #     print("=> ",assoc)           
 

csvFile.close()


# print(type(assoc))
# print(type(tagged_opinions))
# print(type(result))
# print("This are results",results) - # View The NLTK Trees


############################# PART 1b ##################################

###########################   ANALYSIS   ##############################


file = open('input.txt', encoding="utf8")
data_set= file.read()

# print(type(data_set))

opinions=TextBlob(data_set)

noun = opinions.noun_phrases

# print(type(noun))

Counters = Counter(noun) 
most_occur = Counters.most_common(30) 
print(most_occur) 


data = most_occur

n_groups = len(data)

vals_films = [x[1] for x in data]
legends_films = [x[0] for x in data]

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.25

opacity = 0.4

rects1 = plt.bar(index, vals_films, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Ocurrences')


plt.xlabel('Occurrences')
plt.ylabel('Words')
plt.title('Occurrences by word')
plt.xticks(index + bar_width, legends_films)
plt.legend()

plt.tight_layout()
plt.show()















































