import repository

def classifyByCitations(data):
    """ classifies users by their citations

    Args:
        data ([dict]): [data to be classified]
    """

    sum = 0
    for i in data:
        if i['scholar']['citations'] == '':
            i['scholar']['citations'] = 0
        print(type(int(i['scholar']['citations'])))
        sum += int(i['scholar']['citations'])
    avg = sum / len(data)

    threshold = avg/3

    classes = {}
    classes['one'] = []
    classes['two'] = []
    classes['three'] = []

    for i in data:
        temp = {}
        temp['name'] = i['name']
        temp['friends_count'] = int(i['scholar']['citations'])

        if int(i['scholar']['citations']) < threshold:
            classes['one'].append(temp)

        if int(i['scholar']['citations']) >= threshold and int(i['scholar']['citations']) < threshold*2:
            classes['two'].append(temp)

        if int(i['scholar']['citations']) >= threshold*2:
            classes['three'].append(temp)

    repository.writeClassifiedUserByCitationsInFile(classes)
pass

def classifyByFriendsCount(data):
    """ classify users by their friends count

    Args:
        data ([dict]): [data to be classified]
    """
    sum = 0
    for i in data:
        sum += i['friends_count']
    avg = sum / len(data)

    threshold = avg/3

    classes = {}
    classes['one'] = []
    classes['two'] = []
    classes['three'] = []

    for i in data:
        temp = {}
        temp['name'] = i['name']
        temp['friends_count'] = i['friends_count']

        if i['friends_count'] < threshold:
            classes['one'].append(temp)

        if i['friends_count'] >= threshold and i['friends_count'] < threshold*2:
            classes['two'].append(temp)

        if i['friends_count'] >= threshold*2:
            classes['three'].append(temp)

    repository.writeClassifiedUserByFriendsInFile(classes)
pass


if __name__ == '__main__':
    data = repository.getCleanedData()

    classifyByCitations(data)
    classifyByFriendsCount(data)