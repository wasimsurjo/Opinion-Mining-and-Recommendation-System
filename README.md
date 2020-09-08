# Opinion-Mining-and-Recommendation-System

Step 1 (Tokenization):
To extract opinions, our primary step will be to analyze each opinion and extract useful information from it. To do that, we will tokenize every opinion into tokens of words. Let us take the first opinion from our dataset.
“Library should be the strength of a university. It is awesome that we have this perfectly. we can really learn practically. However, we lack open space and place to relax also.” 
We have used the NLTK library of python to tokenize each word from a sentence using its method ‘nltk.word_tokenize (Opinion)’. Other algorithms or methods can be used as well but we have to make sure that every single word is split into tokens and appended to certain indexes of an array or list. Because we will need these tokens for the upcoming procedures. Once every opinion is split into tokens of words, we can now analyze each token and fetch relevant information. 

Step 2 (POS Tagging):
To fetch relevant information from every opinion, we should also know which tokens are essential for us and which are not. 
“My name is Rahim. I think a University should have proper facilities in a library.” 
In the above opinion, the first sentence is not an opinion. We do not need such data for our algorithm. Moreover, “I think a” part of the second sentence is also irrelevant for opinion mining. But we cannot identify such tokens among thousands of opinions if we don’t tokenize and tag each of them. Then with our algorithm expressions, we can filter out relevant opinions from all sentences. So, in this phase, we will tag all tokens from step 1 according to their grammar (Parts of Speech). We will use the NLTK method ‘nltk.pos_tag(opinion)’. This method classifies each token according to the grammar. 
We will see the code and result of the Data Processing phase.





We can see in the results how tokens were generated from the original opinions in step 1 and then the tokens are tagged in step 2. The meaning of the classifications can be generated from the POS table below:


Therefore, ‘Library’ is NNP (Singular Proper Noun), ‘should’ is Modal, etc. In this way, every single opinion is tokenized and tagged in this phase.

Opinion Mining
As we complete the data processing phase, we move on to the next phase of opinion mining. We will execute three more steps here. 1) Chinking 2) Parsing 3) Analysis.

Step 1 (Chinking):
To extract opinions, we have to filter out all unnecessary words from our opinions. There are many ways to do it but we will do chinking. ‘Chinking’ means filtering out certain words based on an expression or grammar. The grammar that we will use is shown below:
Expression: ‘<DT | PP | CD>? <JJ || JJR | JJS> * <NN |NNS |PRP |NNP |IN |PRP \ $> + <VBD |VBZ |VBN |VBP |IN > * <JJ |RB>*<PRP |NN |NNS>*’

With this expression formula, we can fetch a particular segment or phrase from the sentences. We can implement it using regular expressions. 
Here, <DT |PP |CD>? means that we will the sentence based on either a determiner, preposition or a cardinal number. Thereafter, <JJ||JJR|JJS>* means 0 or more adjectives may follow the sentence afterward. Moreover, <NN|NNS|PRP|NNP|IN|PRP\$>+ means 1 or more nouns/prepositions occurrences will be the condition for the validity of the sentence. Furthermore, <VBD |VBZ |VBN |VBP |IN > allows one kind of verb and so on. This grammar will give us useful segments from the sentences. 

Let us consider the opinion below:
“The Library should be the strength of a university. It is awesome that we have this perfectly. we can really learn practically. However, we lack an open space and a relaxing place also.” 
Opinion: 
[‘The’, ‘library’], [‘the’, ‘strength’, ‘of’] [‘a’, ‘university’] 
['It', 'is', 'awesome'] ['that', 'we', 'have']
['we', 'lack', 'open', 'space'] [‘a’, ‘relaxing’, ‘place’, ‘also’]

These are the results from one single opinion, we can get information like that a library is an important factor according to this person. The person is also expressing the opinion of the shortage of space in the university. In this way, we will get several opinions from all the sentences in the dataset.

Step 2 (Opinion Mining):
We will save all the parsed data to a CSV file so that we can use them for analysis. In step 1, we received an opinion regarding the ‘library’. After we analyzing the whole data, we found out that ‘library’ is an important feature demanded by the students and we found some expected qualities like ‘silence’, ‘books’, ‘e-books’ and ‘reading room’ etc. Similarly, we found out concerns regarding ‘campus’. We analyzed the data based on the most repeated noun and adjective using regular expressions and counter. In this way, we can generate much more important information if we collect more data.
As we know, most universities promote their facilities, accommodation, fees, etc. But very few universities will provide concerns regarding the library. So, all the students who desire good library features will miss out universities having great library facilities if he or she searches simply based on ranking or web search. Let us take a look at the code of chinking and parsing.

 

 

After this step, we can use regular expressions and counter the library to extract relevant features. However, there can be several other alternative strategies to extract information. The most important fact is tokenizing, tagging the sentences properly and parsing the tokens efficiently for the opinion mining process.
Step 3 (Analysis):
In the figure above we have seen one opinion extraction only. The same process is repeated for all the opinions in the dataset. This gave us a full dataset containing extracted opinions. The next step is to calculate which issue or topics are most often repeated. By doing so, we can figure out what are the main concerns regarding universities in the mindset of the mass.

Using Textblob in python, we extract all the noun & noun phrases from the whole dataset of extracted opinions. After a little filtering, we were able to generate a list of concerns that were repeated most in the whole dataset. For this demonstration, we will show 7 most repeated concerns that we obtained:

 
Figure: Top 7 issues/demands regarding universities.
NOTE: These values will change every time the dataset is updated. So, none of these results are constant. 
As shown in the above figure, Subject, Campus, Faculties, Education System, Tuition Fees, Extra Curriculum & Lab Facilities are respectively the most repeated concerns in out primary dataset containing 1000+ opinions. We will now use these demands on our recommendation system. It is extremely important to note that these demands may change every time the data set is updated. Therefore, one of the biggest advantages of our system is that it will always be up to date. We will now proceed to the development of a very intelligent recommendation system unlike normal university articles or ranking websites for both students and the teachers.

Recommendation System
As we complete the opinion mining phase, we move on to the next phase of this system. In the Recommendation System, we will conduct two more steps here. 1) Generate Dataset as Per Demand 2) Use TOPSIS Decision Making Algorithm.
Step 1 (Generate Dataset as Per Demand):
Subject, Campus, Faculties, Education System, Tuition Fees, Extra Curriculum & Lab Facilities were the top 7 demands we obtained from our initial opinion mining dataset analysis. Now we will build a new dataset based on two things:
1)	We will collect ratings & opinions from core sources (e.g. official website, university officials)
2)	Opinion of the students & faculties of the particular university.
Based on these two things, all universities will get a rating or score for each demand separately. For this research we will take the top 14 universities from the list with the highest scores among all private universities. Up to 100 people will generate a datasheet containing scores for each demand for every university. Afterwards, a final datasheet is generated based on the average of all the datasheets. It is shown below:



Note: Due to the pandemic COVID-19, the data we were able to collect was very limited. But for obtaining results, it is sufficient. For better results, we will build our datasheets from loads of datasheet in the future.
Step 2 (Use TOPSIS Decision Making Algorithm):
Now that we have obtained a dataset ready to use for recommendation, any person seeking a university some particular demands can search or their own custom set of recommendations based on their required demands instead of a website that contains university ratings. 
For example, according to 4icu.org (Unirank BD), BRAC University is ranked number 1 among the private universities in Bangladesh. But in the figure of university scores, we can see that BRAC University have a lower score then some universities in campus & tuition fees. Now suppose there is a student named Fariha who wants to get admitted to a university with a very good & permanent campus, education system and at the same time, tuition fees matter to her. According to her demands, AIUB & East West University are undoubtedly better choices then BRAC University. But if she only follows the ratings, then she’ll get admitted to BRAC University and then find out that her demands aren’t satisfied properly. For such scenarios, our recommendation system is undoubtedly a revolutionary solution!
But which Algorithm will we use for the recommendation? If the algorithm is not efficient then our recommendation cannot be worth the glory that it claims to have. Therefore, to make sure that the preference generation is reliable, we will use TOPSIS (Technique of Order Preference Similarity to the Ideal Solution).
This method is well recognized not only for finding the shortest distance to the most idea solution but also the longest distance to the most non-ideal solution. We will use TOPSIS method to determine the most idea solution among the 14 universities (Figure) for this demonstration. 
 

For this demonstration we will use 3 choices of Fariha which are Campus (2), Edu. System (4) & Tuition Fee (5). The users can make as many choices as they want and the number of available demands will be increased further with time. After the choices are made, the values of the chosen columns will be sent to the TOPSIS method for the analysis to get 5 best choices among all 14 (The number of choices and Universities can be increased or decreased). The flowchart showing the algorithm of TOPSIS is provided below:


A mathematical demonstration of the TOPSIS decision making algorithm can be found at https://www.slideshare.net/pranavmishra22/topsis-a-multicriteria-decision-making-approach
