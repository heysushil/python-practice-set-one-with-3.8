'''
Inheritance Kya hai?

1. Inheritance ek concept hai jiski madad se hum code ko reuse kar sakte hain.
2. Inheritance OOP's (Object Oriented Programming) ka concetp hai to iska matalb hai ki hum iska use class ke sath hi karenge.
3. Inheritance ek class ke code ko kisi bhi dusre class me use karne ki facility deta hai.
4. Inheritance me hame 2 tarike milte hain:
    a. mutlilevel inheritance
    b. mutlipal inheritance
5. Inheritance me hame 2 tarike ki class milti hain:
    a. parent class: Ye class jiske ke pas sare concept hai.
    b. child class: Ye class jo parent class ke concepts ka use karegi.
6. Inheritance ko asani se samjhne ke liye ise hum kuch is tarike se samjh sakte hain ki:
    a. parent class: dendata (dene wala)
    b. child class: lendata (lene wala)

Multilevel inheritance kya hai?

1. Multilevel inheritance ka use class me ek chaine form me hota hai. Jaie ki a frined hai b ka, b friend hai c ka, c friend hai d ka. Then d indirectly friend hogaya a ka.
2. Yahi same concept multilevel inheritance me use hota hai.
3. Multilevel inheritance me hamesa koi bhi child class kewal single parent class ki properties ko inherit ya use karega.
4. Agar ek child class ek se jada parent class ka use karta hai then is concetp ko 'multiple inheritance kahenge'.

Multiple inheritance kya hai?

1. Yaha par ek child class ek se jada parent class ki properties ka use karta hai.
2. Iske alawa baki multilevel jaisa hi concpet hota hai.
'''

# mutlilevel inheritacne

# create parent class as student
class Student:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
    # student parsonal details
    def studentPersnoalDetails(self):
        # data = {
        #     'name': input('Enter your name: '),
        #     'address': input('Enter your address: '),
        # }

        # return data
        print('\nHi my name is ' + self.name + ' and my address is ' + self.address)

    # student class details:
    def studentClassDetails(self):
        pass
        # data = {
        #     'name': name,
        #     'classRollNumber': input('Enter your roll number: '),
        #     'className': input('Enter your class name: '),
        # }

        # return data
        # print('Hi, my name is ' + data['name'] + ', my roll number is ' + data['classRollNumber'] + ' and my class name is ' + data['className'])

# create object of parent class
# studentobj = Student

# student personal details
# mypersonalData = studentobj.studentPersnoalDetails()

# print('\nHi my name is ' + mypersonalData['name'] + ' and my address is ' + mypersonalData['address'])

# student class details
# myclassData = studentobj.studentClassDetails(mypersonalData['name'])
# print('Hi, my name is ' + myclassData['name'] + ', my roll number is ' + myclassData['classRollNumber'] + ' and my class name is ' + myclassData['className'])

# creating child class for studnet's school detials
class StudentSchool(Student):
    # child class me hame values ko normal hi recive karte hain aur usko aage agar paraent class me pass karna hai to hum use constructer box me hi pass karte hain.
    def __init__(self, **schooldata):
        # pass name and address to parent class constructer
        Student.__init__(self, schooldata['name'], schooldata['address'])
        self.sname = schooldata['sname']
        self.saddress = schooldata['saddress']
        self.sadminName = schooldata['sadminName']
        self.sadminContact = schooldata['sadminContact']

    # school data
    def schoolData(self):
        myschoolData = '''
        ----------------------------------------------
            My School name is {sname}
        ----------------------------------------------
        My school address is {saddress}
        School Admin: {sadminName}
        School Admin contact: {sadminContact}
        ----------------------------------------------
        '''.format(sname = self.sname, saddress = self.saddress, sadminName = self.sadminName, sadminContact = self.sadminContact)

        print('\n', myschoolData)

# data for parent class
name = input('Enter studetn name: ')
address = input('Enter student address: ')
# create object of child class
sname = input('Enter sname name: ')
saddress = input('Enter saddress name: ')
sadminName = input('Enter sadminName name: ')
sadminContact = input('Enter sadminContact name: ')
myschoolDetails = StudentSchool(sname = sname, saddress = saddress, sadminName = sadminName, sadminContact = sadminContact, name = name, address = address)

# call parent class method to show student detials
myschoolDetails.studentPersnoalDetails()

# call child class method
myschoolDetails.schoolData()

'''
Program:

1. SchoolDetail child class me kewal school se realted details hain. Ayse hi kuch aur class banae hain.

2. EK class  class wise subjects ke liye bana hain, yaha par student ke subject ke liye ek method bana hai jaha par multiline string ka use karke student ke sare subjecs show karane hain.

Then is class ke sath me school aur student class ka use karna hai taki sabse pahle school detial then student detail aur then student class detail and then student subject detail show karao.
'''
