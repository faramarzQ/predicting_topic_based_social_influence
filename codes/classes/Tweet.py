import os
import math
import nltk
import numpy as np
from classes import StopWords
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Tweet:
    """
        Tweet Class
    """

    def __init__(self, desired_features):
        """ init method

        Args:
            desired_features ([dict]): [deisired feature to extract from data]
        """
        self.desired_features = desired_features

    def initWithRawData(self, tweet):
        """ initializes object using raw tweet data

        Args:
            tweet ([dict]): [tweet's data]
        """

        for attr in self.desired_features['tweet']:
            if attr in tweet.keys():
                setattr(self, attr, tweet[attr])

        if 'preprocessed_text' in self.desired_features['tweet']:
            self.preprocessText(tweet['text'])
    pass

    def preprocessText(self, text):
        """ preprocesses the text,
            including removing stop words, vectorized tokens,
                detecting it's topic, POS taging words.

        Args:
            text ([string]): [text to be preprocessed]
        """
        self.rawText = text
        self.stoppedText = self.removeStopWordsFromText(text)
        # self.vectorizedText = self.textToVector(self.stoppedText)
        # self.topic = self.detectTopic(self.vectorizedText)
        # self.POSedText = self.POSTagText(self.stoppedText)
    pass

    def removeStopWordsFromText(self, text):
        """tokenizes the text and removes stop words from it

        Args:
            text ([string]): [raw text]

        Returns:
            [list]: [stopped text]
        """
        stopWords = StopWords.StopWords.getStopWords()
        wordTokens = word_tokenize(text)
        stoppedText = [w for w in wordTokens if not w in stopWords]
        return stoppedText
    pass

    def textToVector(self, tokenArray):
        """ converts a tokenized word array into vectors.
            vectorization is done using a triained model by spaCy module,
            link: https://spacy.io/api/token#vector

        Args:
            tokenArray ([list]): [list of tokens]

        Returns:
            [dict]: [victor of each token]
        """
        vectorizedText = {}
        nlp = spacy.load('en_core_web_sm')
        for word in tokenArray:
            vectorizedText[word] = nlp(word).vector
        return vectorizedText
    pass

    def detectTopic(self, vectors):
        """ detect topic of given vectors

        Args:
            vectors ([dict]): [dict of words and their vectors]

        Returns:
            [int]: [vector for topic]
        """
        topic = []
        for index in range(0,96):
            sum = 0
            for word in vectors:
                sum += vectors[word][index]
            avg = sum / 96
            topic.append(avg)
        return topic
    pass

    def POSTagText(self, tokenArray):
        """ specifies part of speech of each token in topken list

        Args:
            text ([list]): [list of tokens]

        Returns:
            [list]: [list containing Part of Speech for tokens]
        """
        return nltk.pos_tag(tokenArray)
    pass

    def getAsDict(self):
        """ returns a dictionary containing the desired attributes of the object

            Returns:
                [dict]
        """
        dic = {}
        for attr in self.desired_features['tweet']:
            if attr in dir(self):
                dic[attr] = getattr(self, attr)

        if 'preprocessed_text' in self.desired_features['tweet']:
            dic['stoppedText'] = self.stoppedText
            # dic['POSedText'] = self.POSedText
            dic['text'] = self.rawText
            # dic['topic'] = self.topic
        return dic
    pass