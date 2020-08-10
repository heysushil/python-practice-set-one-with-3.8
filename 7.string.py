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



'''
Questions:

1. kuch special charaters hai inko dekhna hai:
    , . / \ : ; () {} [] | 
'''
