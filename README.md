#Social Analytics Project

##Packages used ( Python )

#Tweepy:
Download your home timeline tweets and print each one of the texts to the console. Twitter requires all requests to use OAuth for authentication. 

#Praw:
For scrapping comments off reddit

#Potara:
For the purpose of text summarization

#CSV:
The csv module’s reader and writer objects read and write sequences. Programmers can also read and write data in dictionary form using the DictReader and DictWriter classes.

#Pandas:
Pandas is a library providing high-performance, easy-to-use data structures and data analysis tools - https://pandas.pydata.org/

#RE:
This module provides regular expression matching operations similar to those found in Perl.

#String:
The string module contains a number of useful constants and classes, as well as some deprecated legacy functions that are also available as methods on strings. 

#TextBlob:
Perform sentiment analysis by calculating the polarity score

#Preprocessor:
Provides several common utility functions and transformer classes to change raw feature vectors into a representation that is more suitable for the downstream estimators.

#Nltk:
NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum.

#Bs4:
Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.

#DateTime:
The datetime module supplies classes for manipulating dates and times.

#urllib:
This is a package that collects several modules for working with URLs

#Random:
This module implements pseudo-random number generators for various distributions.

#Json:
json exposes an API familiar to users of the standard library marshal and pickle modules.

#Sys:
This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.

#Matplotlib:
Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. 

#Gensim:
Gensim is a free Python framework designed to automatically extract semantic topics from documents, as efficiently
(computer-wise) and painlessly (human-wise) as possible.

#from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS:
The sklearn.feature_extraction module can be used to extract features in a format supported by machine learning algorithms from datasets consisting of formats such as text and image.

#from nltk.tokenize import word_tokenize:
A tokenizer that divides a string into substrings by splitting on the specified string (defined in subclasses).

#from nltk.stem import WordNetLemmatizer:
A processing interface for removing morphological affixes from words. This process is known as stemming.

#from gensim import corpora:
Dictionary encapsulating the mapping between normalized words and their integer ids.

##Installation

The python packages used in this project can be installed using the following commands:

pip install numpy
pip install pandas
pip install nltk
pip install matplotlib
pip install bs4
pip install scikit-learn
pip install tweepy
pip install Praw
pip install Gensim
pip install Preprocessor
pip install Textblob
pip install Potara


math and re libray are built-in python module and do not require any installation


##Project Structure:
|- crawler: Code to crawl from reddit.  
|- Individual Sentiment Analysis Files: Contains the results of our sentiment file in the form of csv.  
|- Modelling for topic. 
|- News data: The csv files for the data collected from reuters and guardians. 
|- Preprocessing: Code for topic modelling pre-processing. 
|- Sentiment Analysis: Code on how the sentiment analysis is being done using textblob. 
|- Sentiment Split: CSv files after pos is being performed. 
|- Social data: CSv files crawled from reddit and twitter based on the topics we have find out. 
