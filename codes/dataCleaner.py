import os
import json

from classes import User
import repository

if __name__ == '__main__':
    """ this file exports cleaned data for each user:
        creates object from each user and their tweets,
        selects given attributes,
        export them in a seperated file for each user

        input: users data with their tweets each in a separate file

        output: users data with selected attribute of each tweet in a separate file
        output: total number of urls in all tweets
    """

    # get list of twitter files
    filesPaths = repository.getTwitterFilePaths()

    desired_features = {
        'user': ['id', 'name', 'favourites_count', 'followers_count', 'friends_count', 'tweets', 'scholar'],
        'tweet': ['id', 'preprocessed_text'],
        'scholar': ['citations', 'hindex']
    }

    single_user_data = {}
    # attach all tweets of each user in a separate file as a json format
    for file in filesPaths:
        single_user_data['users'] = {}
        with open(file) as jsonFile:
            tempTwitterFile = json.load(jsonFile)
            userObj = User.User(desired_features)
            userObj.initWithRawData(tempTwitterFile)
            single_user_data = userObj.getAsDict()

            # write cleaned data in file
            repository.writeCleanedUserJsonToFile(single_user_data, userObj.name)

            del userObj
pass
