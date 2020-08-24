'''
Python Collections:

Ye 4 datatypes multiple values ko hold ya store karne ki capacity rakte hain. Is liye hi inhe collection bhi kha jata hai.

Example: Abhi tak humne int,float,comple aur set datatype use kiya but ye sabhi ek time pe ek value ko hi store kar sakte hain.

Isliye jab hame ek sath multiple values ko store karna ho single varibale me to hum yehai 4 datatypes ka use karte hain.

1. list => denote by []
2. tupe => ()
3. dict (dictonary) => {}
4. set => {}

Python List me following methods hain:

Note: Example ke liye mylist = [1,2,3,4], iske behalf par examples diye gaye hain:

1. append(): List me last se 1 nai value add karne ke liye append ka use kiya jata hai. Example: mylist.append(5)
2. clear(): clear method list ko empty karta hai. Empty karne par agar varibel ko print karoge to empty list milega. But error nahi milega. Example: mylist.clear()
3. copy(): Copy method ek list ko copy karke new variable me store kar dega. Example: newlist = mylist.copy()
4. extend(): Extend ka use karke ek se jada list ko aapsh me marge kiya jata hai. Exaple: mylist.extend(newlist)
5. index(): Index method kisi bhi value ka index position bata hai. Example: mylist.index(4)
6. insert(): Insert method list me existing index possition par new value ko update karta hai. Example: mylist.index(1, 11), yaha par(indexPossion, newValue)
7. pop(): Pop method thik append ka ulta hai. Ye by default list me last se ek value ko remove karta hai. Otherwise kisi specific index value ko remove karne ke liye is method me index postion dena hota hai. Example: mylist.pop() - Ye last se ek value remove kardega. mylist.pop(2) - Ye list ke 2nd index ki value ko remove kardega.
8. remove(): Remove ka use kiya jata hai jab aapko index postion ki jagh par value ka pata ho. To direct value ko remove karne ke liye remove method ka use karte hain. Example: mylist.remove(4) - Ye list me jaha bhi 4 hai useko remove karega.
9. reverse(): Reverse list ko ulta kardega. Means list by default assending order me hota hai. To ye list ko desending order me convert kar dega. Example: mylist.reverse()
10. sort(): Sort mehtod list ko assending order me sort kardega. Example: mylist.sort() yaha par sort(revers=Ture/False) Ture = Ye list ko desending order me sort karega. False = Ye assending order me sort karega.
11. count(): Count method list me present kisi bhi dublicate values ko count karne ke liye use hota hai. Example: mylist.count(4)
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

mylist = []
mylist.append(11)
mylist.append(21)
mylist.append(31)
mylist.append(41)
mylist.append(41)

newlist = mylist.copy()
seclist = mylist.copy()
mylist.clear()
count = newlist.count(41)
extend = newlist.extend(seclist)
newlist.insert(0, 111)
newlist.pop()
newlist.pop(0)
newlist.remove(41)
# newlist.reverse()
newlist.sort(reverse=True)
print('\n\nMylist: ',mylist)
print('\n\nNewlist: ',newlist,' Count:41: ',count)
print('\nIndex: ',newlist.index(41))
# print('\nInsert: ',newlist.insert(0, 111))

