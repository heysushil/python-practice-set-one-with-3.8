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

'''
Question:

Note: Sare program for loop ka use kar ke banae hain.

1. 1 to 100 number print karna hai.

2. user se input lena hai koi bhi single number and uska table (Pahada) print karan hai. Aur iska range 10 tak rahega.

ये हिन्दी गिनती है: १ २ ३ ४ ५ ६ ७ ८ ९ १०

3. User se 2 input lena hai ek staring point aur 2nd end point ke liye aur usko print karna hai.
    
    Important Point:

        a. Agar user first input greater then second number de raha hai then usko message show karna hai ki ye possible nahi hai.
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
'''