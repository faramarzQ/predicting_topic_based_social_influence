import os
from classes import Tweet
import json

class User:
    """
        User class
    """

    def __init__(self, desired_features):
        """ init method

        Args:
            desired_features ([dict]): [deisired feature to extract from data]
        """
        self.desired_features = desired_features
    pass

    def initWithRawData(self, data):
        """ initialises the object with the desired features

            Args:
                data ([array]): [raw data: user, tweets, followes, ...]
                desired_features ([dict]): [desired feature to extract]
        """

        for attr in self.desired_features['user']:
            if attr in ['id', 'name']:
                setattr(self, attr, data[0][attr])

            if attr in ['favourites_count', 'followers_count', 'friends_count']:
                setattr(self, attr, data[1]['followers'][0][attr])

        if 'tweets' in self.desired_features['user']:
            self.tweets = {}
            for i in range(len(data)):

                if(i not in [0, 1, 2]): # object 0, 1 and 2 are not tweets

                    # init a tweet object
                    tweetObj = Tweet.Tweet(self.desired_features)
                    tweetObj.initWithRawData(data[i])

                    self.tweets[data[i]['id']] = tweetObj
    def getAsDict(self):
        """ returns a dictionary containing the desired attributes of the object

            Returns:
                [dict]
        """

        dic = {}
        for attr in self.desired_features['user']:
            if attr in dir(self):
                dic[attr] = getattr(self, attr)

            # init tweets in dict if desired
            if 'tweets' in self.desired_features['user']:
                dic['tweets'] = {}

            for index in self.tweets:
                if 'tweets' in self.desired_features['user']:
                    dic['tweets'][str(index)] = self.tweets[index].getAsDict()
        return dic
    pass