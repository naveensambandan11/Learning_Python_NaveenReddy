class Firstclass():
    a = 100
    def __init__(self):
        print("This is self method or constructor")

    def Method_1(self):
        print("my first method")

obj1 = Firstclass()
obj1.Method_1()
print(obj1.a)