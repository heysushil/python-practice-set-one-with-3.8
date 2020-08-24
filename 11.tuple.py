'''
Python Tuple:

1. Tuple nonchange hai, aur list changeable hai. iska systax ()
2. Tuple me values na change kar pane ki wajah se isme is tarike ke koi bhi methods nahi milte hai.
3. Single value wale tuple me value ke sath ek comma dena jaruri hai otherwiese wo ek stirng ya int value hi hoga.
4. List ke jaise hi tuple me same to same slicing follow hota hai. Ye posstive and negative dono me hota hia.

Tuple me total 2 mehtods milte hain:

Note: Example tuple - newtuple = (11,22,33,33)

1. count(): Same list count() method jaisa hi hai. Is ke use se tuple me exist dublicate values ko count kiya jata hai. Example: newtuple.count(33)
2. index(): Same list index jaisa hi hai. Tuple me kisi bhi value ka index posstion find karne ke liye index method ka use kiya jata hai. Example: newtuple.index(33)
'''

mytuple = ('Hello',)
print('\nCHeck type of mytuple: ',type(mytuple))

mynexttuple = (2,3,4,5,6,7)
# mynexttuple[0] = 22
print('\nmynexttuple[0]: ',mynexttuple[0])

# tuple to list convertion:
tuple2listValue = list(mynexttuple)
tuple2listValue[0] = 22
mynexttuple = tuple(tuple2listValue)

print('\nmynexttuple[0]: ',mynexttuple[0])
print('\nmynexttuple[0]: ',mynexttuple)

'''
For syntax: 

for initialization in values:
    print or other work

PHP For loop sysntax:

for(intialization;condtion;increment/decrement){
    for boody;
}
'''
myclass = ('Ram','Shyam','Radha')

for m in myclass:
    print('Name: ',m)

# condtion to check student is presenet or not
student = input('Enter student name: ')
    
if (student in myclass) == True:    
    print('\nYes, '+ student + ' is present.')
    # print('\nCheck Anjali is present or not: ',student in myclass)
elif len(student) <= 2:
    print('\nStudent, your name is to sort make it long.')
else:
    print('\nNo, '+ student + ' is not present.')

# delete tuple
aclass = myclass
del myclass
print('\nCLass list: ',aclass)

# joining
bclass = ('Arjun','Nakul','Bheem','Ram')

bigclass = aclass + bclass
print('\nBigclass: ',tuple(bigclass))

# tuple me 2 methods use hote hai: index() count() [0]
print('\nIndex: ',bigclass.count('Ram'))

newtuple = (11,)
print('\n',type(newtuple))

'''
HM:
1. Jaise list me index values find kiya tha waise hi yaha tuple me karna hai.
2. Jaise index ki slicing ki thi ex: [0:2] yahi same kaam tuple me karna hai.
3. Jaise lise me negative slicing ki thi waise hi same yaha karna hai.
'''