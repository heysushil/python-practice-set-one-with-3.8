# sting
'''
Sting ko use karne ke tarike:

1. single line sting single (') ya double qoute (") se use kiya jata hai.
'''

mystr = "main single line string hu."
print('\n',mystr)
mysting = '''
Mian first multiline string hu
stirng hame 2 type ki milti hai

1. single line sting
2. multi line stirng
'''
print('\n',mysting)
myothersting = """
Main other multin sting hu

hello multiline
sting
        ---
        how
        ---
                @@@ 
                are
                @@@
                        you            
                    
"""
print('\n',myothersting)

# string 2 int convert
mystr = '33'
print('\nstring 2 int convert: ',int(mystr),' type: ',type(int(mystr)))

# sting 2 float
# int 2 sting
# float 2 string

mynumber = input('\n\nEnter your mobile number: ')
print('\nmynumber type: ',type(mynumber),'\nMynumber in interger: ',int(mynumber),'\nmynumber type in int: ',type(int(mynumber)))


# stirng with format
name = 'Ram'
print('''
My number with string value: {}
Mynumber type: {}
Mynumber convert 2 int type: {}
My Name: {}
'''.format(mynumber, type(mynumber), type(int(mynumber)), name))

# user input check then show
name = input('User input value for check or not: ')

# For checking string value is digit or not by isdigit()
forDigit = name.isdigit()
print('\nFor check user input is Digit: ',name.isdigit())

# name.isalnum() use to check stirng contain number and alphaets both
print('\nname.isalnum() use to check value is alphabet+num: ',name.isalnum())

# name.isdecimal() to check in string that the value is b/w 0-9 value or not
print('\nname.isdecimal() chekc value is b/w 0-9: ',name.isdecimal())

# name.isalpha() to check value is aplhabet: 
print('\nname.isalpha() to check value is aplhabet: ',name.isalpha())

print('\nname.islower() use to check alphabet is in lowercase: ',name.islower())

print('\nname.isupper() use to check aplha is in upper case: ',name.isupper())

print('\nname.istitle() use to check string first char is upper case: ',name.istitle())

# print(name.is)

# print(name.isdigit());exit()
# bool() and type()
# using strings isdigit() to find values is digti or not by True or False

if name.isdigit() == True:
    print('\nInterger value not allowed in name.')
elif name.islower() == True:
    print('\nAll lower case in name not allowed') 
elif name.isalnum() == True:
    print('\nNumber and char both not allowed in name.')   
else:
    print('\nHi, ',name)

# stirng slicing or indexing
print('\nFirst char of name: ',name[0], name[1], name[2])
# Anjli (n-1) [star:end] (end-1)
print('\nName range:[0:4] ',name[0:4])
print('\nName range:[:4] ',name[:4])
print('\nName range:[0:] ',name[0:])

# string possion in negative
# alwasy possitive slicing run from left to right
# Negative slicing run from right to left
print('\nName range:[-1] ',name[-1])
print('\nName range:[-3:-1] ',name[-3:])

# find value length by len()
print('\nName length: ',len(name))

# strip() use to remove staring and eding spaces from sting
print('\nName: ',name)
print('\nRemove staring n eding space: ',name.strip(),'New len: ',len(name.strip()))

# using lower() to convet all in lower case
print('\nName in lower case: ',name.lower())
print('\nName in upper: ',name.upper())
# hi HI Hi myfirstname my_first_name myFirstName my_First_Name
print('\nName in camaple case: ',name.title())

# replace
print('\nPython change to Py: ', name.replace('Python','Py'))

# split use to break the string
print('\nSplit name: ',name.split(' '))

# chekc word in string by in opertation
print('\nCheck python is in name or not: ','python' in name)
print('\nCheck python is in name or not: ','python' not in name)

'''
Questions:

1. kuch special charaters hai inko dekhna hai:
    , . / \ : ; () {} [] | 
'''
