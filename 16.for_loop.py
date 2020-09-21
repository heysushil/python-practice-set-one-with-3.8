'''
For loop ka work behavior:

1. For loop ka use kisi bhi sequacne ko print karne ke liye use hota hai.
2. Jaise ki hamare pas list, tuple, set and dictionary hai joki values ko sequence me dete hain.
3. Jaise ham ek example lete hain aur use print karke check karte hain.

For loop ka syntax:

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
'''

mylist = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7]
print('\n')

print(len(mylist))
# mylist.sort()
print(mylist[-1])
print(mylist.index(7))
# exit()
# mylist.
print('\nFor loop: ')
for n in mylist:
    print('No: ', n, ' | position => ', mylist.index(n))

# next loop
print('\nFor loop using string')
nameList = ['ram','shyam','anjali','oindrila','radha']

for name in nameList:
    print('My name is ' + name)

# use rang in loop: range(start, end)
for number in range(1,51):
    print(number)

# nested loop: means loop ke andar loop
fields = ['name','mobile','address']
names = ['ram','shyam']

for f in fields: # 3 index
    # print('Fiels Name: ', f)
    for n in names: # 2 index
        print(f, ' : ', n)
    
    print('\n')

'''
nested for loop case:

f=name : names=ram
f=name : names=shyam

f=mobile : 

for start hua: range(1, 5)
    for start hua: (1, 5)

'''
a2d = ['a','b','c','d']

for a in a2d:
    for r in range(1,6):
        print(a, ' : ', r)

# fiels and thire data
fields = ['name','mobile','address']
names = ['ram',9989879879,'India']

for f in fields:
    for n in names:
        print(f, ' : ', n)

# use else in for loop
for i in range(1, 6):
    print('Number: ', i)
else:
    print('Finally our for loop of print number is finded.')

'''
Question:

Note: Sare program for loop ka use kar ke banae hain.

1. 1 to 100 number print karna hai.

2. user se input lena hai koi bhi single number and uska table (Pahada) print karan hai. Aur iska range 10 tak rahega.

ये हिन्दी गिनती है: १ २ ३ ४ ५ ६ ७ ८ ९ १०

3. User se 2 input lena hai ek staring point aur 2nd end point ke liye aur usko print karna hai.
    
    Important Point:

        1. Agar user first input greater then second number de raha hai then usko message show karna hai ki ye possible nahi hai.
        2. Agar user input me number ki jagha alphabets deta hai to bhi user ko message show karna hai ki ye posible nahi hai pleas enter only number.
        3. Finally agar user inputs sahi deta hai then user ko wo complete range ka numebrs show karane hai.

Note: Question number 4 ke liye reserch ki jarurat padegi.

4. List me last index number kya hai ye pata karna hai? List me last value kya hai ye nahi pata karna hai. But...
    Example:
        Is list me [1,2,3,4,5,6,7,8]
        Last index postion 7 hai.
    Case:
        a. Ye case sabse pahle ek number list me without dublicate valeus ke last index position find karna hai.
        
        b. But agar list me multiple dublicate values hain then is list ka use karke ye pata karna hai ki last 7 ka index number kya hai:
        [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7]

5. 2 list hain jinke data ko side by side show karan hai:
    Example lists:
        fields = ['name','mobile','address']
        names = ['ram',9989879879,'India']

    For loop ka use karke inko side by side show karna hai?

6. Jaise for loop me else ka use kiya gaya hai wise hi while loop me user se 2 numebrs ka input lena hai aur in case agar starting number 1 se greater hai to number not accetp ka message show karan hai.

Otherwise agar end number greater then 10 hai to not accept ka mesage show karan hai.

Otherwise numbers ko print karna hai and at last while loop end ke bad else ka use karke while loop stoped ka message show karna hai.
'''

# number = 'hello'
# print('\n', number.isdigit())
# num2 = 'hi by'
# if number.isdigit() == True:
#     print('\n', number.isdigit())