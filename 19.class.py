'''
Class ke bare me jankari:

1. Class ko use karne ke liye 'class' keyword ka use kiya jata hain.
2. Jaise fucntion me function ko use karne ke liye fucntion call karte hain waise hi yaha par class ko use karane ke liye 'object' banate hain.
3. Jaise single function me ek kisi work ko complete kiya jata hai. Wise hi class multiple functions aur  attributs or variables ka collection hota hai.
4. Jaise normal case me hum ek fucntion ko function kahte hain. Wise hi ek function class me as a 'method' kaha jata hain.
5. Hum class me variables ko 'attributs' kahte hain.

Note: Class ka first character hamesa capital letter me hona cahiye.
'''

# create simple class
class MyFirstClass:

    name = 'Anjali'
    # user function
    def myname():
        print('\nHello my first function.')

    def myname1():
        print('\nHello my first11111 function.')

# create object to use class
myobj = MyFirstClass

myobj.myname()
myobj.myname1()

print('\nHi, ', myobj.name)

'''
Question:

1. Class ke andar 4 fucntion work behaviour ke liye fucntion create karne hai apne hisab se aur unka result dekhna hai:

    a. Function without arguments & without return value
    b. Function with arguments & without return value
    c. Function without arguments & with return value
    d. Function with arguments & with return value

2. Ek class banana hai Restorant name se aur iske andar alag-alag disess ke liye fucntion create karne hai aur unme apne hisab se print message use kanr hai.
'''