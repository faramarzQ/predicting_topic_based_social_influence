import os
import json
import os.path

file_directories = {
        'tweeter_data_import': '/home/faramarz/Documents/coding_projects/predicting_topic_based_social_influence/data_sandbox/twitter/data/',
        'scholar_data_import': '/home/faramarz/Documents/coding_projects/predicting_topic_based_social_influence/data_sandbox/scholar_data/',
        'cleaned_data': '/home/faramarz/Documents/coding_projects/predicting_topic_based_social_influence/data_sandbox/cleaned_data/',
        'classified_data': '/home/faramarz/Documents/coding_projects/predicting_topic_based_social_influence/data_sandbox/classified_data/',
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
    with open(file_directories['cleaned_data']+str(id)+".json", "w") as file:
        json.dump(data, file)
pass

def getUserScholarByUserAttr(attr):
    """ get scholar data of user with it's name
        (file name of user's scholar is his/her name)

    Args:
        name ([string]): [user's name]
    """
    filePath = file_directories['scholar_data_import']+attr+'.json'

    if os.path.isfile(filePath):
        with open(filePath) as jsonFile:
            data = json.load(jsonFile)
    else:
        data = None
    return data
pass

def getCleanedData():
    data = []
    for r, d, f in os.walk(file_directories['cleaned_data']):
        for file in f:
            with open(file_directories['cleaned_data']+file) as jsonFile:
                    data.append(json.load(jsonFile))
    return data

def writeClassifiedUserByFriendsInFile(data,):
    """ write users which classified by their friends count

    Args:
        data ([dict]): [user's data]
    """
    with open(file_directories['classified_data']+"classified_user_by_friends_count.json", "w") as file:
        json.dump(data, file)
pass

def writeClassifiedUserByCitationsInFile(data,):
    """ write users which classified by their citations

    Args:
        data ([dict]): [user's data]
    """
    with open(file_directories['classified_data']+"classified_user_by_citations.json", "w") as file:
        json.dump(data, file)
pass