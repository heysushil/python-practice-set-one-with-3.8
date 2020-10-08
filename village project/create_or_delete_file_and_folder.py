'''
Yaha par file handling realter work solve kiya gaya hai:

1. create new file
2. update new file
3. delete file
4. create folder
5. delete folder
'''
import os

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
