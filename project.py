class Calc():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def Add(self):
        c = self.a + self.b

        return c
    
    def Sub(self):
        c = self.a - self.b

        return c
    
    def mul(self,a,b):
        ans = a * b

        return ans
    
res = Calc(15,5)
print(res.Add())
print(res.Sub())
print(res.mul(5,5))