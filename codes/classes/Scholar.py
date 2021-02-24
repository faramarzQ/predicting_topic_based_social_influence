import os
import json

class Scholar:
    """
        Scholar class
    """

    def __init__(self, desired_features):
        """ init method

        Args:
            desired_features ([dict]): [deisired feature to extract from data]
        """
        self.desired_features = desired_features
        self.empty = False
    pass

    def initWithRawData(self, data):
        """ initialises the object with the desired features

            Args:
                data ([array]): [raw data: user, tweets, followes, ...]
                desired_features ([dict]): [desired feature to extract]
        """
        if data == None:
            self.empty = True
            return

        for attr in self.desired_features['scholar']:
            if attr in data.keys():
                if data[attr] == '':
                    data[attr] = 0
                setattr(self, attr, int(data[attr]))
    pass

    def getAsDict(self):
        """ returns a dictionary containing the desired attributes of the object

            Returns:
                [dict]
        """
        dic = {}

        if self.empty == True:
            return dic

        for attr in self.desired_features['scholar']:
            if attr in dir(self):
                dic[attr] = getattr(self, attr)
        return dic
    pass