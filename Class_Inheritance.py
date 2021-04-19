from Class_2 import Firstclass
class Childclass(Firstclass):
    c = 1000
    def __init__(self):
        print("ths is constructor of child class -- ")
        Firstclass.__init__(self,5,8)

    def Method_2(self):
        print("this is childclass method")
        #self.Method1()

    def Method_2_Addition(self):
        return self.c + self.a + self.b

obj2 = Childclass()
obj2.Method_2()
print(obj2.MethodAddition())
print(obj2.Method_2_Addition())