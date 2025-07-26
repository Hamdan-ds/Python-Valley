class MoverLoading:
    def __init__(self,a,b,c,d,e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    def sum(self,a,b):
        tot = a + b
        print("SUM of a & b:", tot)

    def sum(self,a,b,c):
        tot = a + b + c
        print("SUM of a,b,c:", tot)

    def sum(self,a,b,c,d):
        tot = a + b + c + d
        print("SUM of a,b,c,d:", tot)

    def sum(self,a,b,c,d,e):
        tot = a + b + c + d + e
        print("SUM of a,b,c,d,e:", tot)

    def sum(self,*args):
        for x in args:
            print(x,end=" ")

obj1 = MoverLoading(1,2,3,4,5)

obj1.sum(2,3)
obj1.sum(2,3,4)
obj1.sum(2,3,6,8)
obj1.sum(2,3,5,7,8)
obj1.sum(1,2,3,4,5,6,7,8,9,11,22,33,44,55)