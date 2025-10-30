# Sum 1
# Create a class Calculator with methods :
# add(a,b)
# subtract(a,b)
# multiple(a,b)
# divide(a,b) -->handle divide by zero using try...except

class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addition(self):
        x = self.a + self.b
        print(x)

    def subtracts(self):
        y = self.a - self.b
        print(y)

    def multiple(self):
        x = self.a * self.b
        print(x)

    def divide(self):
        try :
            y = self.a / self.b
            print(y)
        except:
            print("Error in division")

result = Calculator(10,20)

result.addition()

