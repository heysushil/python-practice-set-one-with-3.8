'''
Set in python:

Important points to set:

1. Set ko {} is braket se denote karete hain.
2. Set values ka koi order nahi hota hai. Means values ko agar index position ke behalf par feach karna caho to error milega.
3. Set me values hamesa unique honge.
4. Set values hamesa suffle karte rahete hain.

Set ka use collection of set me se dublicacy remove karne ke liye kiya jata hai.

Set ka use ek se jada set ko apas me mager karn ke liye aur sath me dublicate valeus ko filter karne ke liye kiya jata hai.
'''

# create a noraml set
set_a = {1,2,3,4,5,6,7,8}

# check datatype of myset
print('\nCehck datatype: ', type(set_a))

# chekc is set index work or not
# print('\nGet 1 by index of set_a: ', set_a[1])

# print set_a
print('\nset_a: ', set_a)

# check particular value is present in set or not
print('\nCheck 1 is avalibale in set or not: ', 1 in set_a)

# add single value in set by add()
set_a.add(9)
print('\nAdd 9 in set: ', set_a)

# add a multiple values at once in set so use update()
set_a.update([10,11,12])
print('\nAdd multiple values in set: ', set_a)

# find a length of set by len()
print('\nCheck len of set: ', len(set_a))

# remove values from set by remove()
# when try to remove same number again you will get KeyErro for handling that error you need another method: discard()
set_a.remove(12)

# get user input to remove values form set
# number = input('Enter number b/w 1 to 12: ')
# set_a.remove(number)
print('\nDelete 12 from set a: ', set_a)

# For handline error regarding unavailable value use discard()
set_a.discard(11)
set_a.discard(11)
print('\nDiscard 12 again: ', set_a)

# for removein vlaue we also use pop() but remember set have not index facility so that you don't know which value is on last field.
set_a.pop()
print('\nPop: ', set_a)

# copy set to anohter varaible by copy()
set_b = set_a.copy()
print('\nset b: ', set_b)

# for empty the set use clear()
set_a.clear()
print('\nset a: ', set_a)

# del keyword use to delete ka set_a
del set_a
# print(set_a)

# new set for joing
set_a = {2,4,6,8,0,11,13,15}

# join 2 set using union()
print('\nset a: ',set_a)
print('\nset b: ', set_b)

set_c = set_a.union(set_b)
print('\nset c',set_c)

# update method use to mearge set b in set a
set_a.update(set_b)
print('\nset a: ', set_a)

# check set_b is subset of set a or not
print('\nIs set_b, subset or set_a: ', set_b.issubset(set_a))

# check set a is super set of set b
print('\nCheck set a is subper set of set b: ', set_a.issuperset(set_b))

# check difference
diff = set_a.difference(set_b)
print('\nDifference: ', diff)

# intersecation
inter = set_a.intersection(set_b)
print('\nInter: ', inter)