'''
Condition statments and practicale

Sytanx:

1. Jab single condition hoto:
    if(your_condtion):
        your message. ye string ho ya kuch bhi ho sakta hai.

2. Jab single condition ho and ek default condtion ho to:
    if(your_condtion):
        your message. ye string ho ya kuch bhi ho sakta hai.
    else:
        your default message will be here.

3. Jab 1 se jada condition ho to:
    if(your_condtion):
        your message. ye string ho ya kuch bhi ho sakta hai.
    elif(your_another_condition):
        your message.
    else:
        default condition message.

4. Nested condition:
    if (your_condtion):
        Yaha par message dena chao to do ya nahi.

        if(condtion):
            your message.
        else:
            your message.
    else:
        default condition message.

Comparision conditional operations:

Note: Yaha par a aur b variable le kar example show kiya hai.

1. Equals: a == b
2. Not equals to: a != b
3. Less then: a < b
4. Less then or equal to: a <= b
5. Greater then: a > b
6. Greater then or equal to: a >= b
'''

# Use only if
a = 20
b = 10

# Check if a > b
if a > b:
    print('\nGreate, a is greater then b.')

# Condtion banao and show else not if
if a < b:
    print('\nYes a is less then b.')
else:
    print('\nOhhhh, no a is not less then b.')

# multiple condtion a = 20, b = 10
if a < b:
    print('\nYes a is less then b.')
elif a <= b:
    print('\nYes mightbe a is lessthen or equal to b.')
elif a > b:
    print('\nYes a is greater then b.')
else:
    print('\nOhhhh, no a is not less then b.')

# nested condtion
if a > b:
    print('\nYes a is greater then b.')

    # neded condtion
    c = 20
    if a == c:
        print('\nGreate a is == c')
    else:
        print('\nIn nested else condtion not satifyed.')
else:
    print('\nNon of the condtions satisfyed.')

'''
Use case:
if anjali present then show present message
    then check anjalis homework then
        if anjali completed homework then show homework done message
        else send messagae to parents
other wise else if anjali not presenet then show absent message
'''
student_present_in_class = ['anjali','oindrila','sushil']
student_name = input('\nEnter your name: ')

# in this case we get true if value present
if student_name in student_present_in_class:
    print('\nYes, sir I\'m present '+ student_name + '.')
    # check studetn homework
    check_homework = input('Enter y/n for homework: ')
    if check_homework == 'y':
        print('\nGreat ' + student_name + ', you did a great job.')
    elif check_homework == 'n':
        print('\n' + student_name + ', you must call your parent.')
    else:
        print('\n' + student_name + ' sudhar jao nahi to pitai hogi. Sahi input do?')
else:
    print('\n'+student_name+' is not present in class.')


    
'''
Programmes for practice:

1. User se 2 input lo and check karo ki agar 1st input bada hai to useke liye message show karo otherwise second ke liye message show karo.

2. Ek shoping list banao, aur iske bad me check karo ki shoping list me who iteam hai ya nahi hai jo tum shop par jane ke bad shopkeeper se puch rahe ho. Iske liye product varaible create karna and then check karna hai.

Agar item list me hai then shopkeeper se uska price pucho?
Then agar price acceptable hain means yes or not wala case?
Then item mo purchase karo and show item bill, jisme ki-
    1. Item purchase date
    2. Item order number
    3. Item Price
    4. Iteam name
Included ho. Is ouput ko representative way me show karna hai.
'''
