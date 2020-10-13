'''
Yaha par file handling realter work solve kiya gaya hai:

1. create new file
2. update new file
3. delete file
4. create folder
5. delete folder
'''
import os

# Get Admin choise from main.py file
class AdminChocie():
    def __init__(self, choice):
        self.choice = choice

    # Admin choice ko check karene ke liye
    def checkAdminChoice(self):
        if self.choice == 1:
            print('\nShowing list of villages: ')
            self.showAllVillages()
        elif self.choice == 2:
            print('\nCreate new village: ')
            self.createNewVillage()
        elif self.choice == 3:
            print('\nWork exit.')
        else:
            print('\nAdmin, aapnew wrong choice enter kiya hai. Pleas enter 1 or 2.')

    def showAllVillages(self):
        # Check village list
        villagelist = open('village project/village_list.txt', 'r')
        getVillageList = villagelist.read()
        # check condtion if village_list.txt is empty then create new village otherwise show list of village
        if bool(getVillageList) == True:
            # call Filhanding class to cerate new village folder
            print('\nVillage list: \n', getVillageList)
        else:
            # Create new village
            print('\nAbhi koi bhi village nahi creat kiya gaya hai. Pahle new village create kariye.\n')
            self.createNewVillage()

    def createNewVillage(self):
        # create new village
        villageName = input('\nEnter new village name: ')
        # add village name on village_list.txt
        checkfile = open('village project/village_list.txt', 'r')
        getFileData = checkfile.readlines()
        
        if villageName+'\n' not in getFileData:
            villagelist = open('village project/village_list.txt', 'a')
            villagelist.write('\n' + villageName)
            villagelist.close()
        checkfile.close()

        # Condtion for check village exists or not
        try:
            os.mkdir('village project/' + villageName)
        except FileExistsError:
            print('\nVillage [ ' + villageName + ' ] is already exists. Try with new name.')
            # Agar file exist karta hain then again provide choicse to dmin.
            getAdminChoice()
        else:
            print('\nVillage [ ' + villageName + ' ] is created successfully.')
            # Show choices again
            getAdminChoice()      

# Sab se pahel admin se choice get karna hai uske liye funciton
def getAdminChoice():
    '''
    Chocies:
        1. Show villages
        2. Create new village
    '''
    try:
        choice = int(input('\n\nEnter your choice:\n1 - Show Village list\n2 - Create new village\n3 - Exit\nEnter (1/2/3): '))
    except ValueError:
        print('\n\nYou must enter only interger numbers.')

        choice = int(input('\n\nEnter your choice:\n1 - Show Village list\n2 - Create new village\nEnter (1/2): '))
    finally:    
        mychoice = AdminChocie(choice)
        mychoice.checkAdminChoice()

getAdminChoice()


'''
Pending works:

1. New file name se create ho raha hai, in case agar village me same name se 1 se jada log hain then error milga. Isko handle karna hai.
'''
