'''
File handling kya hai? Kya work hota hai?

1. file handling normal jaise hum system me files create karte hai. Wahi same work hum python ke help se karenge.
2. EK file ke case me hum:
    1. file ko create karna
    2. file ko read karna
    3. file ko update karna
    4. file ko delete karna

File handling ka work:

1. File handling me 4 methods mostly use hote hain:
    1. open()
    2. read()
    3. write()
    4. close()
2. Sab se pahle hum file ko open karte hain. Is case me file open karne ke sath kuch methods use karne hote hain:
    1. open() method me second argement as 4 alag tarike ke arguments pass kar sakte hain:
        1. 'r': file read ke liye, error if file not exists
        2. 'a': append - create file if not exists
        3. 'w': open file for write, create file if not exists
        4. 'x': create file, if file exists get error
    2. open() method me 2 aur arguments milte hian:
        1. 't': text - ye by default text mode ke liye hota hai
        2. 'b': binary - multimedia format (e.g: image)
'''

# open file with read mode but file abhi hain nahi to filenotfound ka error milega.
# open('file handling/myfirstFile.txt', 'r')

# open file in read mode using a argument, in case if file not exists then 'a' will creat it.
# open('file handling/myfirstFile.txt', 'a')

# open file in write mode so that we write someting in file
myfile = open('file handling/myfirstFile.txt', 'a')

mydata = '''
Anjali padhlo abhi bhi time hai.
'''

myfile.write(mydata)
myfile.close()

# open file again and read it
readMyFile = open('file handling/myfirstFile.txt', 'r')
# read() comple file ko read karne ke liye
# print(readMyFile.read())

# read(10): number of charater read karne ke liye
# print(readMyFile.read(10))

# readline(): use to read single line
# print(readMyFile.readline())
# print(readMyFile.readline())
# print(readMyFile.readline())

print(len(readMyFile.readlines()))

readMyFile.close()

exit()

# use w to overwirte the file content.
name = input('Enter your name: ')
myNextFile = open('file handling/' + name + '.txt', 'w')
mydata = 'Ye hamara pahle w mode file hai.'
myNextFile.write(mydata)
myNextFile.close()

readMyNextFile = open('file handling/' + name + '.txt', 'r')
print(readMyNextFile.read())
readMyNextFile.close()

'''
Program:

1. ek class create karo Stduent name ki jisme ki:
    1. student detail method: is method me student ki detail get karo. Like as student name, parents name, school and class name.
    2. student ki ye sari details student name ki file bana kar usme store karna hai.
    3. is ke liye student name se ek folder bana hai jisme jistne bhi sutdnets ka registration hoga unka name wise file create hota rahe.
    4. is work me error handling use karna hai aur ye check karna hai ki student sahi field me sahi information put kar raha hia ya nahi. Like as student name me agar student number add kar raha hai to error message show karo otherwise aage badho.
'''