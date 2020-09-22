'''
Class constructer:

1. Constructer asal me ek special function / method hai.
2. Isko use karne ke liye __init__() iska use kiya jata hai.
3. Ye ek sath sabhi mulitple methods me same number of arguments ko pass karne ke liye use hota hai.
4. constructer me hum sabhi arguments ko 'self' keyword ka use kar ke inko self instance bana dete hain.
5. 'self' ek tarike ka variable hai jo multiple values ko hold kar sakta hai.
'''

class Calculater:
    # create constructer
    def __init__(self, num1, num2):
        self.n1 = num1
        self.n2 = num2
        # custom value
        self.name = 'Anjali'
    # addition method
    def addition(self):
        sum = self.n1 + self.n2
        # sum = 100 + 200
        print('\nHi, ', self.name)
        print('\nAddition: ', sum)

    # subtraction method
    def subtraction(self):
        sub = self.n1 - self.n2
        print('\nHi, ', self.name)
        print('\nSubtraction: ', sub)

    # multiplication method
    def multiplication(self, num1, num2):
        mul = num1 * num2
        print('\nMultiplication: ', mul)

# create object of class
result = Calculater(500, 300)
# call addition
result.addition()
result.subtraction()
result.multiplication(10, 20)


# anohter class
class MyData:
    def __init__(self, data):
        self.name = data[0]
        self.course = data[1]
        self.address = data[2]

    def myInfo(self):
        data = '''
        Hello team my name is {}
        I'm learing {} and my address is {}.
        '''.format(self.name, self.course, self.address)
        return data

# create object
data = ['Anjali','Python','India']
userdata = MyData(data)

# call myinfo fucntion
print('\n', userdata.myInfo())

'''
Questions:

1. del keyword ka use karke try karna hai.
2. Class create karna hai aur uske andar constructer create karna hai. Ye work charo fucntion work behaviour ke sath use karne hain.
Programm ki choice aap ki hai.
'''