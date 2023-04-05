class Student:
    def __init__(self):
        self.name=input("enter your name")
        self.usn=input("enter usn id")
        self.age=int(input("enter your age"))

    def display(self):
        print("name : ",self.name)
        print("usn : ",self.usn)
        print("age : ",self.age)

class Ugstudent(Student):
    def __init__(self):
        Student.__init__(self)
        self.sem=input("enter semester")
        self.fees=input("enter fees")
        self.stipend=int(input("enter stipend"))
        Ugstudent.display(self)
    def display(self):
        Student.display(self)
        print("sem : ",self.sem)
        print("fees : ",self.fees)
        print("stipend : ",self.stipend)

class Pgstudent(Student):
        def __init__(self):
            Student.__init__(self)
            self.sem = input("enter semester")
            self.fees = input("enter fees ")
            self.stipend = int(input("enter stipend"))
            Pgstudent.display(self)

        def display(self):
            Student.display(self)
            print("sem : ", self.sem)
            print("fees : ", self.fees)
            print("stipend : ", self.stipend)


while(True):
    print("1.UG Student \n 2.PG Student \n 3.Exit")
    ch=int(input("enter your choice "))
    if ch==1:
        obj1 = Ugstudent()

    elif ch==2:
        obj2 = Pgstudent()

    elif ch==3:
        exit()

    else:
        print("enter valid input")
