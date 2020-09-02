'''
Python me Loop ka use and work case.

Python me hame 2 loop case milte hain.

1. while loop
2. for loop

Note: Waise other programming languages like C, C++, PHP me hame 3 loop case milte hain. For, while, do-while. Also C, C++ jaise lanagauge me increment (++) aur decrement (--) use hota hai but python me ye use nahi hota hai.

Loop ka use kyo karte hain?

1. Loop same type ke repated work ke liye use hota hai.
2. Sequence datatype - list, tuple, range ye values ko index form me sotore rakhte hain. Inka use loop me values ko one by one print karne ke liye kiya ja sakta hai.
3. Ya fir kisi bhi collection of data like database table data ko bhi hum loop ke through print kara sakte hain.
4. Loop me pre aur post increment aur decrement hote hain.

While loop ka syntax:

intilization
while (condtion):
    body of while loop

While loop syntax ke baare me:

1. Intilization me koi bhi starting point decide karna hota hai. Like i = 1, Becasue loop ko hamesa starting and ending point ki need hoti hai.
2. while (i <= 10): Ye condtion hogi ki loop ko kaha tak chalna hai.
3. While body: yaha par jo kuch bhi print karna hai ya fir koi loop ya condtion chalana hai. Wo sab kuch yaha par kiya ja sakta hai.

For loop syntax:

for intilization in collectionOfValues:
    body of for loop

For loop syntax ke baare me:

1. For loop me intilization kewal variable ka hoga isme koi bhi value assign nahi karna hai. Becasue jo collection values hai usme se one by one values intilization ko recive hoga and wo usko for loop ke body ko pass karega.
2. Collection of values: Ye koi bhi collection ho sakta hai. Like as:
    a. list collection
    b. tuple collection
    c. range collection
    d. database tabel data collection
    e. so on....

If aur while loop me difference?

1. If Condtion agar sahi hai to wo condtion body me aayega aur wahi work stop ho jayega.
2. While loop me jab tak condtion sahi hai tab tak loop chalta ranega.
'''

# while loop ka use
start = 1
# start = 1 2 3 4 5
# preincrement = 2
while(start < 5):
    # Print start value = 1
    start += 1
    print('\n',start)
    # increment start by 1
    # start = start + 1
    # start += 1

# setps of while loop

i = 1 # setup 1
while i < 5: # setup 2
    print(i) # setup 3 to print value
    i += 1 # setup 4 to increment i by 1 untile loop false
    print('\nFinally while stoped.')

# use list in while loop
print('\n\n')
userlist = ['ram','shyam','radha','seeta']
i = 0
while i < len(userlist):
    print(userlist[i])    
    # use condtion to stope when get shyam
    if 'shyam' == userlist[i]:
        print('\nHi', userlist[i])
        # break
    i += 1

i = 0
while i < len(userlist):
    print('Hi, ' + userlist[i] + ', welcome to loop. Hope you enjoy the loop?')
    i += 1


'''
While loop programs:

1. 1 to 10 Number print karna hai.

2. 1 to 50 number print karna hai but jab 25 number mile to hame ek alg print message show karn hai 25 numbre ke liye using condtion.

3. Ek list create karo aur usme apne friedns ka name include karo then agar first friend aaye to usko hello hi message show karna hai. Second friend aaye to usse colleage ke bareme puchna hai. Thired fried aaye to susse jo man kare wo puch lena. Yaha par multiple condtion ka use karna hai. Sath me isme sabhi friend ko while loop karne ke show karn hai.

4. Ek list create karna hai jisme ki alphabets honge aur unko while loop ka use karke print karna hai but jab bhi koi vovel aaye to usko batan hai. Yaha par while loop and condtion use hoga. Yaha par single if condtion me ye kaam karna hai iske liye multiple condtion nahi use karna hai.
'''

name = 'Oindrila hello hi'
print(name.count('hi'))