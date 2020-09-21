'''
Lambda Function ke bare me:

1. Ye ek anonymous function hai.
2. Lambda function me hum multiple arguemts de sakte hain. But iss fucntion ke andar kewal single expression diya ja sakta hai.

Lambda fucntion Syntax:

lambda numberOfArguments : your expression
'''

# define lambda fucniton
result = lambda a, b: a + b

# call lambda fucntion with the help of result
# result(10, 20)
print('\nResult: ', result(10, 20))


# function me lambda ka use
# define fucntion
def mynum():
    # yaha par num 
    return lambda lamNum: lamNum + 300

'''
Function and lambda ka work folow:

1. sab se pahle fucntion ko call kiya
2. fucntion call me 'num' 
'''
mylamFunctionCall = mynum()

# mylamFunctionCall(100)
print('\nmylamFunctionCall(100): ', mylamFunctionCall(100))


'''
Question:

1. Keyword aur fucntion me kya difference hain?
2. Python me total kitne keywords hai?
3. Python me total kitne pre-defined functions hain?
4. Python me identifires kya hain?
'''