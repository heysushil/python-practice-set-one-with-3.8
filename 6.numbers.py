# number system:
'''
1. int 
2. float
3. complex
'''

# int: negative ya possitve non-desimal numebrs are interger number
# print ke andar single ya double colonm ke anader hum chahe jitne space de sakte hai
# print ke andar hum new line ke liye \n use karte hai
# agar hum dusir line me code likna chate hai aur uske liye print me hi enter press karte hai to error show hoga
myFirstIntVaraible = 10
# stringValue = '\nmyFirstIntVaraible: '
print('\nmyFirstIntVaraible: ', myFirstIntVaraible)

# sum of 2 inter values
a = 10
b = 20
mysum = a+b
# print('SUm answer: a = ',a,' , b = ',b,' and sum = ',mysum)
print('a + b = ',mysum)
print('check value a: ', type(a))

# float
myfloat = 22.22
print('myflaot type: ',type(myfloat))


# complex: yaha par kisbhi int ya flot value ke sath small j addon hota hai, jo value ko complex value banata hai.

mycomplex = 22.66j
print('mycomplex type: ',type(mycomplex))


'''
kaise
1. int ko float me convert kare?
2. flaot ko int me convert?
3. int to comlex convert?
'''

intval = 33
int2floatConvert = float(intval)
print('int2floatConvert type: ',type(int2floatConvert))
print('int2floatConvert: ',int2floatConvert)

# float 2 int
floatVal = 22.22
print('floatVal type:=- ', type(floatVal),' || floatVal: ',int(floatVal))

# int or float 2 complex
print('int2comlex: ',complex(intval))
print('float2comlex: ',complex(11.11))

print('comple2int: ',int(3j))

'''
Python me type conversion ko casting kahte hai.

'''