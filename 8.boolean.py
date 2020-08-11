'''
Boolean: True / False

1. True ke case me hamesa 1 ya 1 se greate koi bhi value true case me aati hai
2. False ke case me empty, null ye false case
'''

print('\n',10)
name = 'Simran'
print('\nUse bool(): ',bool())

# hame user ka name recive karnege agar user name me kuch bhi nahi likh raha hi to ham false recive karenge ya fir true

# <input type="text" name="username">
# name = post['username']
name = input('Enter your name: ')
print('Your name is ',name, bool(name))

# cech boolean
if name != "":
    print('\nWelcome ',name, ' to python class.')
else:
    print('\nYou are not included.')

'''
1. Boolean me in kuch cases me hi hame False multa hai:

bool(False)
bool(None)
bool(0)
bool("")
bool([]) List
bool({}) dict
bool(()) tuple
'''