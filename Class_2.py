class Firstclass():
    a = 100
    b = 200
    def __init__(self,b,c):
        print("this is constructor")
        self.firstnum = b
        self.secondnum = c

    def Method1(self):
        print("this is first method")

    def MethodAddition(self):
        return self.a + self.firstnum + self.secondnum + Firstclass.b

obj1 = Firstclass(2,3)
obj1.Method1()
print(obj1.MethodAddition())