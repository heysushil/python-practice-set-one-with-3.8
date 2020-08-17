'''
len() use for geting the lenght of variable
'''

# > or ==
if (10 > 10 or 10 == 10) and (10 < 11 or 11 >= 15):
    print('\nHello if')
else:
    print('\nHi else')

name = input('Enter your name: ')
print(len(name))
# mobile email
# error handling regex len()


print(type(name))
# exit()
if type(int(name)) == int:
    print('\nInterger value not allowed in name.')
else:
    print('\nHi, ',name)
