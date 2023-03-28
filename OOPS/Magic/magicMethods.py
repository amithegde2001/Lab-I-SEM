class ope:
    def __init__(self):
        self.l1 = []

    def accept(self):
        n=int(input("enter a number"))
        for i in range(0, n):
            ele=int(input("enter element"))
            self.l1.append(ele)
        print("list = ", self.l1)

    def __add__(self, other):
        newli=[]
        for i in range(0, len(self.l1)):
            newli.append(self.l1[i]+other.l1[i])
        print("after addition : ", newli)

    def __sub__(self, other):
        newli=[]
        for i in range(0, len(self.l1)):
            newli.append(self.l1[i]-other.l1[i])
        print("after subtraction: ", newli)

    def __mul__(self, other):
        newli=[]
        for i in range(0, len(self.l1)):
            newli.append(self.l1[i]*other.l1[i])
        print("after multiplication: ", newli)

    def __floordiv__(self, other):
        newli=[]
        for i in range(0, len(self.l1)):
            newli.append(self.l1[i]//other.l1[i])
        print("after floor division :", newli)