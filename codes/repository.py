import os
import json

file_directories = {
        'tweeter_data_import': '/home/faramarz/Documents/coding_projects/predicting_topic_based_social_influence/data_sandbox/twitter/data/',
        'scholar_data_import': '/home/faramarz/Documents/coding_projects/predicting_topic_based_social_influence/data_sandbox/scholar_data/',
        'cleaned_data_export': '/home/faramarz/Documents/coding_projects/predicting_topic_based_social_influence/data_sandbox/cleaned_data/',
    }

def getTwitterFilePaths():
    """ returns array of path for all twitter's files in specified directory

    Returns:
        [array]: [array of file paths]
    """
    filesPaths = []
    for r, d, f in os.walk(file_directories['tweeter_data_import']):
        for file in f:
                if '.json' in file:
                    filesPaths.append(os.path.join(r, file))
    return filesPaths
pass

def writeCleanedUserJsonToFile(data, id):
    """ write user and it's tweets in a file, named with user's id

    Args:
        data ([dict]): [user's data]
        id ([int]): [user's id]
    """
    with open(file_directories['cleaned_data_export']+str(id)+".json", "w") as file:
        json.dump(data, file)
pass