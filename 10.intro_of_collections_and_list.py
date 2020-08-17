'''
Python Collections:

Ye 4 datatypes multiple values ko hold ya store karne ki capacity rakte hain. Is liye hi inhe collection bhi kha jata hai.

Example: Abhi tak humne int,float,comple aur set datatype use kiya but ye sabhi ek time pe ek value ko hi store kar sakte hain.

Isliye jab hame ek sath multiple values ko store karna ho single varibale me to hum yehai 4 datatypes ka use karte hain.

1. list => denote by []
2. tupe => ()
3. dict (dictonary) => {}
4. set => {}
'''

# List
listvalue = [2,3,4,5,6,7]

print('\nListvalues: \n\n',listvalue)
# check listvalue datatype
print(type(listvalue))
# get 2 by index
print('Get 2 by index possition: ',listvalue[0])
# get negaitve index posstion values for number
print('Negative numebr: listvalue[-1]: ',listvalue[-1])

# set names in list
names = ['Ram','Shyam']
print('name[0]: ',names[0])
print('names[1]: ',names[1])

# get index values by negative index posstion
# always by defult list run by left to right
# but in negative case list run by right to left
print('Negative names[-1]: ',names[-1])
print('Negtive names[-2]: ',names[-2])

'''
1. List multiple values ko hold karsakta hai
2. index value
3. list index 0(zero) se start hota hai.
'''

# get list range index values. ye list 4 index values hold kiya hai
myNewList = ['Ram','Shyam','Radha','Geeta']
# in list box [start:end-1]
print('myNewList[0]: ',myNewList[0:4]) # always rembere index end is (n-1)
# define only start in list
print('By start posstion only: ',myNewList[2:])
# define only end
print('Provide end posstion: ',myNewList[:5])
# negative list range
print('Negative range: ',myNewList[-3:])

'''
List IMP Points:

1. Kewal list, list values ko change kar sakta hai.
'''
nums = [2,3,4,5,6]
# change 2 values
nums[0] = 20
nums.insert(1,30)
# add new value in list
nums.append(22)
nums.append(20)
# count any values in list
print('Count 20 in list: ',nums.count(20))
# add one list to another list
otherlist = [7,8,9,0]
nums.extend(otherlist)
# for remove list vauel by thire name
nums.remove(20)
# remove value by index posstion
nums.pop(2)
# by defalut remove last posstion value
nums.pop()
# dublicate the lsit or copy the list
duplicatelist = nums.copy()
print('duplicatelist: ',duplicatelist)
print('Nums values: ',nums)
# empty list or clear the list values
nums.clear()
# nums.
# parmanent delete the list
del nums

# print('Nums values: ',nums)



