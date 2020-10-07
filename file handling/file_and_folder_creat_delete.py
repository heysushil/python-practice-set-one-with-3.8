# delete file using os library
import os

# step 1
# studentname = input('Enter student name: ')
# if bool(studentname) == True:
#     path = 'file handling/' + studentname + '.txt'

#     # delete the file
#     os.remove(path)

#     print('\nYour file ' + studentname + '.txt is deleted successfully.')

# check if file exists or not then delete
studentname = input('Enter student name: ')
filepath = 'file handling/' + studentname + '.txt'

if os.path.exists(filepath):
    # delete the file
    os.remove(filepath)

    print('\nYour file ' + studentname + '.txt is deleted successfully.')
else:
    print('\nYour file ||| ' + studentname + '.txt ||| is not found try again.')

# create new folder
# os.mkdir('file handling/newfolder')
os.rmdir('file handling/newfolder')



