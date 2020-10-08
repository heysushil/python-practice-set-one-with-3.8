'''
New familty count or new village create concept:

1. sab se pahle check karte hain ki admin ko kya kaam karna hai.
2. Admin options:
    1. Choose 1 - Register new family on village
    2. Choose 2 - Create new village
'''

import create_or_delete_file_and_folder as f

class AdminChocie():
    def __init__(self, choice):
        self.choice = choice

    def checkAdminChoice(self):
        if self.choice == 1:
            # print('\n\n1. Choose 1 - Register new family on village')
            # file.create_or_delete_file_and_folder
            myf = f.Filehandling('demo','demo')
            myf.createNewFile()
        elif self.choice == 2:
            print('\n\n2. Choose 2 - Create new village')
        else:
            print('\n\nYou chooced wrong choice. Pleas try again and enter 1 or 2.')


# pass admin choice
try:
    choice = int(input('\n\nEnter your choice:\n1 - Register new family\n2 - Create new village\nEnter (1/2): '))
except ValueError:
    print('\n\nYou must enter only interger numbers.')

    choice = int(input('\n\nEnter your choice:\n1 - Register new family\n2 - Create new village\nEnter (1/2): '))
finally:
    mychoice = AdminChocie(choice)
    mychoice.checkAdminChoice()





'''
Pending works:

1. checkAdminChoice() function me else ke bad redirect karan hai wapas usi funciton me.
'''