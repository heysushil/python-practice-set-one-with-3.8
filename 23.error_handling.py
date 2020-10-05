'''
Error Handling concept:

Error handling me 4 block of area use kiya jata hai:

1. try: code ko yaha par check kiya jata hai
2. except: code agar sahi hai then yaha par aayega
3. finally: at last sub close karne ke liye
4. else: last message show karane ke liye

Raise keywork ka use:
1. raise keywork ka use single line error handle ke liye kiya jata hai.

Multiple errors:

1. syntax error
2. type error
3. intentation error
4. ModuleNotFoundError
'''

name = 'Hello python'
try:
    print(name)
except NameError:
    print('\nName variable abhi nahi banaya gaya hai.')
except:
    print('No value recevied.')
else:
    print('Sab kuch badhiya hai.')


try:
    print(name + 798798)
except TypeError:
    print('\nOnly interger number allowed for addition.')
else:
    print('Hello elese')
finally:
    # finally ka use file handling me file close karne ke liye use karte hain
    # kisibhi work ko finllay exit karne ke liye be iska use kiya jata hai.
    print('\nFinally our work is completed.')


# use of raise
# if 3 < 5:
#     # print('hello 3 < 5')
#     raise Exception("Yaha par, less then 5 number accepted nahi hai.")

# check value
if not type(name) is int:
    # print('hello')
    raise TypeError('String not allowed')

