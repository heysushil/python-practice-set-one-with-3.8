'''
Dictionary in Python:

About Assosiative Array:

1. C, C++ ya php me hame assosiative array milta hai.
2. Synatx: variableName = array('name' => 'Sushil')
3. Assosiatve sysntax me array(key => value)
4. Yahi same concept of associative array python me Dictionary ke name se use hota hai.

Python me dictionary ko use karne ke liye:

1. Syntax: newvalue = {'key or userDefinedName' : 'value or userDefinedValue',}
2. Tupel me () small bracke ke agar koi single value define ki jaye to wo tuple type nahi hai because tuple ke liye last me comma dena jaruri hai.
3. Waise hi dictionay me {} ke andar key:value ke bad comma dena jaruri hai. Other wise same braket ka use set me bhi hota hai. Aur dono confilt ho jata hai.
'''

userData = {'name':'Sushil',}
print('\ncheck userDataType: ', type(userData))

# define multiple key values in dict
userData = {
    'name' : 'Hey Sushil',
    'course' : 'python',
}

print('\nUser data: ', userData)

# how to get name from dict
name = userData['name']
print('Name: ', userData['name'])

# use dict get method to get value
print('\nGet name from userdata: ', userData.get('name'))

# udpate a dict key value using direct by key
userData['name'] = 'Sushil'
print('\nUpdated name: ', userData)

# find length of dict using len()
print('\nFind lenght of userdata: ', len(userData))

# add new key value in dict
userData['address'] = 'India'
print('\nAdd new value in userdata is address: ', userData)

# remove value from dict using pop() with key name in bracket
removeByPOP = userData.pop('course')
print('\nremoveByPOP: ', userData)

# to remove the last value form dict use popitem() method
removeLastByPop = userData.popitem()
print('\nremoveLastByPop: ', userData)

# using del keyword you'll delete key of dict
del userData['name']
print('\nUserdata: ', userData)

# using del to delete the userdata variable
del userData
# print('\nUserdata', userData)

# create new dict for furter experiments
data = {'name' : 'Python', 'work' : 'programming',}

# copy the dict in new varaible
backupData = data.copy()
print('\nBackup Data: ', backupData)

# clear the dict using clear method
data.clear()
print('\nAfter clearing the data: ', data)

# use case of nested dict
userData = {
    'anjali' : {
        'mobile' : 89879798,
        'address' : 'India',
    },
    'oindrila' : {
        'mobile' : 9998989,
        'address' : 'IND',
    },
}
print('\nNested UserData: ', userData)

# get anjalis mobile number from nested dict
print('\nMobile: ', userData['oindrila']['mobile'])


# Get values by user and store them in dict
name = input('Enter your name: ')
course = input('Enter your course name: ')

# user input name will provide dynamic values on dict
# dynamic value means always the values will new or changes
# static value will be non changable. Like as above example
userData = {
    'name' : name,
    'course' : course,
}

details = 'Hi, ' + userData['name'] + ' Details\n\nName: ' + userData['name'] + '\nCouser: ' + userData['course']

print('\n', details)