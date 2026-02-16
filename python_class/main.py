class Calculator():
    #constructor
    def __init__(self, a,b):
        self.a = a
        self.b = b
    # methods
    def add(self):
        return self.a + self.b
    
    def subtraction(self):
        return self.a - self.b
    
    def multiple(self):
        return self.a * self.b
    
    def division(self):
        return self.a / self.b
    


myCalc = Calculator(2,3)

myCalc.add(4,5)
myCalc.subtraction(5,30)

        
