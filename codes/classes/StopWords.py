from nltk.corpus import stopwords

class StopWords:
    __instance = None

    def __init__(self):
        """ create stop words lists using singleton Design patter

        Raises:
            Exception: [description]
        """
        if StopWords.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            stopWords = set(stopwords.words("english"))
            stopWords.update(['.', ':', ',', '?', ')', '(', '[', ']', '}', '{', '!', '@', '#', '$', '%', '%', '&' ,'*', '_', '+', '=', '/', '-', '\'\'', '``', '""', 'n\'t', 'http', 'https', '\'s'])
            StopWords.stopWords = stopWords
            StopWords.__instance = self
    pass

    def getStopWords():
        """ returs list of stop words

        Returns:
            [list]: [stop words]
        """
        if StopWords.__instance == None:
            StopWords()
        return StopWords.stopWords
    pass
