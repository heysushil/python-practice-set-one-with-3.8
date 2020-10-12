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
class AdminChocie(Filehandling):
    def __init__(self, choice):
        self.choice = choice


    def checkAdminChoice(self):
        # 1 for creating new family file
        if self.choice == 1:
            # print('\n\n1. Choose 1 - Show village list.')
            # show all villages name
            villagelist = open('village project/village_list.txt', 'r')
            getVillageList = villagelist.read()
            # check condtion if village_list.txt is empty then create new village otherwise show list of village
            if bool(getVillageList) == False:
                # call Filhanding class to cerate new village folder
                pass
            else:
                # show all village list
                pass

        elif self.choice == 2:
            # 2 for create village folder
            print('\n\n2. Choose 2 - Create new village')
        else:
            print('\n\nYou chooced wrong choice. Pleas try again and enter 1 or 2.')

# File handling to create new file or folder            
class Filehandling():
    def __init__(self, *userinput):
        self.fileName = userinput[0]
        self.folderName = userinput[1]

    def createNewFile(self):
        path = 'village project/' + self.folderName + '/' + self.fileName
        
        try:
            newfile = open(path, 'x')
        except FileExistsError:
            print('\n', ' family already exists. Try again with unique name.')
        except:
            print('File already exists.')
        else:
            print('\n', newfile , ' family created successfully.')
        



'''
Pending works:

1. New file name se create ho raha hai, in case agar village me same name se 1 se jada log hain then error milga. Isko handle karna hai.
'''
