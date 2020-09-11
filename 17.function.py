'''
About Function in Python:

Function 2 type ke hote hain:

    1. pre-defined function
    2. user-defined function

Pre-defined function: 

1. Ye function programming lanaguage me pahle se define hote hain.
2. In work aur behaviour pahle se set hota hai.
3. Jaise ki example ke liye: print() function.
    a. print function python me output show karne ke liye use hota hai.
    b. Is funciton me number of aruments ka use kiya jata hai.
    c. Jaise ki print me hum direct math solve kar sakte hain.
    d. Koi dusra pre-define fucntion bhi use kar sakte hain. Jaise ki datatype check karne ke liye type() function.
4. Har pre-define fucntion ka work behaviour bilkul user-define function jaisa hi hota hai. Bas in funciton ko pahle se hi define kar diya gaya hai.
5. Jin funciton ya work behavious ko pahle se define nahi kiya gaya hai. Un ke liye hi hum user-define fucniton create karte hain.

User-defined function:

Note: funciton create karne ke liye 'def' keyword ka use karte hain.

1. User-define funciton ka name user define karta hai.
2. Funciton name hamesa relevent name hona cahiye. Taki name se function ka work behaviour pata chale.
3. Function ke sub types bhi hain:
    a. Function with arguments & with return value
    b. Function without arguments & without return value
    c. Function with arguments & without return value
    d. Function without arguments & with return value
4. Funciton ka work kisi bhi specific problem ko solve karne ke liye kiya jata hai.
5. Ek funciton ke andar aap multiple condtion, loops, function ya class tak call kar sakte hain.

Function ka syntax:

def your_function_name():
    funciton body

Funciton name ke limitations:

1. Fucntion name ko bhi create karte time varibale ke rules ko dhyan rakho.
2. Jaise new variable number se ya fir space se nahi start kar sakte ho. Same to same yaha par bhi wahi sare varaible ruls follow hote hain.

Note: Yaad rahe complete programming lanaguage me hame 2 chije bar bar milti hain.

1. Keywords: Jaise ke del, def, class etc...
2. Function: Jaise ki print(), if(), for() etc....

Function me argument aur return ka matlab:

1. Argument asal me ek simple varaibel jaisa hi hai. Jab bhi hum fucntion me argument ki baat karte hain. To iska matlab hota hai ki hum kuch varible ya values fucntion me recive kar rahae hain.
2. Because function me hum koi bhi ek specific work karte hain aur uska result show karate hain ya fir result ko return karte hain.
3. Jaise hamesa yaad rakho ki arguments ko funciton me recive hi kiya jayega. Waise hi jab bhi function koi work complete kar dega then yata result fucniton me hi show karado. Ya fir result ko return bhi karaya ja sakta hai.
4 Jab bhi bat result ko return karane ki ho, iska matlab hoga ki hum wo resutl funciton ke bahar recive karenge. Then usko kisi varibel me store kar sakte hain.

Static aur dynamic values ka matlab:

1. Static values means ye fix values hain jo hum ek bar define kar diye wahi rahega.
2. Dynamic values means jab hum user input ke through valeus recive karte hain use time user kuch bhi values de sakta hain.
'''

# Ye only fucntion defintion hai.
# Kewal fucntion create karne se iska output nahi dekh sakte ho.
def myFirstFucntion(): # ye fucntion definition hai
    print('\nHello first function.')

# Function ko use karne ke liye use call karna jarui hai.
# myFirstFucntion() # ye fucntion call hai


# Function without arguments & without return value: using create addition funciton

# function
def addition():
    firstNumber = 50
    secondNumber = 100

    sum = firstNumber + secondNumber
    print('\nSum: ', sum)

# call addition()
# addition()

# Function with arguments & without return value
def functionWithArguments(n, e):
    # name = 'Oindrila'
    print('Hi, ' + n + ' your emial id is ' + e)

# function call
'''
Yaha par funciton me 1 argument name define kiya gaya hai, issi liye jab fucniton ko call kiya jayega to usme ye name argumen pass karna jaruri hai.
'''
# name = input('Enter your name: ')
# email = input('Enter your emial id: ')
# functionWithArguments(name, email)
name = 'my name'
# functionWithArguments(name,'your email')

# function with list argumest
def sumFucntion(data):
    print('type: ', type(data))
    print('Hi ' + data[0] + ' and ' + data[1])

# pass list on funciton
# data = [1,2,3,4,5]
data = ['ram','shyam']
# sumFucntion(data)

# in case recive normal data in tuple form in fucniton
'''
Function me unexpected number of data recive karna ho to hum usko  * ka use karke as a tuple form me recvie kar sakte hain.
'''
def fucntionWithStar(*userdata):
    print('type: ', type(userdata))
    print('Hi, ' + userdata[0] + ' and ' + userdata[1])

# fucntionWithStar('ram','shyam','radha')

'''
Recive unexpected number of details in the form of key value pare then hame ** double start ka use karn hai aur values ko as dictionary ke formate me funciton me recive karna hai.
'''
def fucntionWithDictinaryValues(**name):
    print('fucntionWithDictinaryValues type: ', type(name))
    print('Hi fucntionWithDictinaryValues your data is ', name['name'] + ' . Your email id is ' + name['email'])


fucntionWithDictinaryValues(name='Anjali', email='myemial@')


# Function with arguments & with return value

# Function without arguments & with return value


'''
Questions:

1. Ek funciton create karna hai jisme ki apne firneds ki list dict ke form me bana hai aur usko fucntion ko pass karna hai. Then fucntion me usko multi line string ka use karke apne sabhi friends ak detail show karan hai.
'''
