dict={}
class Student:
    def __init__(self):
        self.usn=input("enter usn id")
        self.name=input("enter name")
        self.age=int(input("enter age "))

    def display(self):
        print("usn : ",self.usn)
        print("nam : ",self.name)
        print("age : ",self.age)

class child1(Student):
    def __init__(self):
        Student.__init__(self)
        self.sem=input("enter sem")
        self.sub=[]
        self.total=0
        for i in range(1,6):
            subb=int(input(f"enter mark for sub {i}"))
            self.sub.append(subb)
            self.total+=subb

        self.per=(self.total/250)*100;
    def display(self):
        Student.display(self)
        print("sem : ",self.sem)
        print("marks : ",self.sub)
        print("total marks : ",self.total)
        print("percentage : ",self.per)

class child2(child1):
    def __init__(self):
        child1.__init__(self)
        dict.update({self.name:{
            "name ":self.name,
            "usn ":self.usn,
            "age ":self.age,
            "sem ":self.sem,
            "marks ":self.sub,
            "total marks ":self.total,
            "percentage ":self.per,
        }})

def printdict():
    for key in dict:
        print(key,dict[key])

while(True):
    print("1.add \n 2.display \n 3.exit")
    ch=int(input("enter your choice "))
    if ch==1:
        ob=child2()

    elif ch==2:
        printdict()

    elif  ch==3:
        exit()

    else:
        print("enter valid input ")