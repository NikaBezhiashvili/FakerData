"""
Task Description:
Imagine that you have comments on posts,
where the whole data is getting stored in different datasets (users, posts, comments, etc.)

TODO:
1. Generate files & info - users, posts, comments
2. Store information across files
3. Check Every single particle (perfectionism)

MUSTS!
USER QUANTITY MUST BE 1,000,000 ROW
COMMENTS QUANTITY MUST BE 10,000,000 ROW

"""

from faker import Faker
import pandas as pd
from random import randint

""" Functions """


def generate_user(generated_id):
    """
    Generates user data
    :param generated_id: given unique id
    :return: single user data as dict (for dataframe)

    """
    fakeObject = Faker()
    firstName = fakeObject.first_name()
    lastName = fakeObject.last_name()
    userName = firstName + lastName + str(randint(1970, 2023))
    address = fakeObject.address()
    contact = fakeObject.phone_number()

    dataFrame = pd.DataFrame([{
        'userId': generated_id,
        'firstName': firstName,
        'userName': userName,
        'address': address,
        'contact': contact
    }])


    return dataFrame


def add_user(fileName:str, data):
    """
    inserts generated userdata into given file, it's not necessary to check if file exists because
    pandas - to_csv procedure has exception if os.path.isfile = False it creates new one at given destination
    so checking that path is valid is waste of resources

    :param fileName: destination
    :param data: userdata:
    :return: inserts userdata to destination
    """
    try:
        getFile = pd.read_csv(f'DataFiles/{fileName}.csv')
        getFile._append(data, ignore_index=True)
        data.to_csv(f'DataFiles/{fileName}.csv', mode='a', header=False)
    except:
        data.to_csv(f'DataFiles/{fileName}.csv')




def generate_comments(fileName):
    """
    Generates user comments
    :return: user/comment reference
    """


    fakeComment = Faker()
    userId = randint(1,1000000)
    comment = fakeComment.paragraph(nb_sentences=2)

    commentData = pd.DataFrame([{
        'userId': userId,
        'comment': comment
    }])

    try:
        getFile = pd.read_csv(f'DataFiles/{fileName}.csv')
        getFile._append(commentData, ignore_index=True)
        commentData.to_csv(f'DataFiles/{fileName}.csv', mode='a', header=False)
    except:
        commentData.to_csv(f'DataFiles/{fileName}.csv')




if __name__ == '__main__':
    userQuantity = 1000000
    commentQuantity = 10000000
    for i in range(1, userQuantity):
        add_user('test', generate_user(i))
    for i in range(1, commentQuantity):
        generate_comments('commenttest')
