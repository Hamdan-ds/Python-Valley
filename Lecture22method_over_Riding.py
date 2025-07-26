
class Parent:
    def test(self):
        print("It's a Parent Class Test Method")



class Child(Parent):
    def test(self):
        print("IT's a Child Class Test Method")

obj1 = Child()
obj1.test()
# obj1.work()