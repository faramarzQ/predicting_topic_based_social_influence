import json
import os

from classes import User

if __name__ == '__main__':
    """ this file exports cleaned data for each user:
        creates object from each user and their tweets,
        selects given attributes,
        export them in a seperated file for each user

        input: users data with their tweets each in a separate file

        output: users data with selected attribute of each tweet in a separate file
        output: total number of urls in all tweets
    """

    file_directories = {
        'raw_data_import': '/home/faramarz/Documents/coding_projects/SICTR/data/test',
        'cleaned_data_export': '/home/faramarz/Documents/coding_projects/SICTR/data/test_filtered_data/',
    }

    # import names of json file in the given directory
    filesPaths = []
    for r, d, f in os.walk(file_directories['raw_data_import']):
        for file in f:
                if '.json' in file:
                    filesPaths.append(os.path.join(r, file))

    desired_features = {
        'user': ['id', 'name', 'favourites_count', 'followers_count', 'friends_count', 'tweets'],
        'tweet': ['id', 'preprocessed_text'],
    }


    data = {}
    single_user_data = {}

    # attach all tweets of each user in a separate file as a json format
    for file in filesPaths:
        single_user_data['users'] = {}

        with open(file) as jsonFile:
            tempFile = json.load(jsonFile)
            userObj = User.User(desired_features)
            userObj.initWithRawData(tempFile)

            single_user_data = userObj.getAsDict()

            # write user and it's tweets in a file, named with user's id
            with open(file_directories['cleaned_data_export']+str(userObj.id)+".json", "w") as file:
                json.dump(single_user_data, file)

            del userObj
pass
