from magicMethods import *

ob1 = ope()
ob2 = ope()

ob1.accept()
ob2.accept()

while True:
    print("1.Addition \n 2.Subtraction \n3.Multiplication \n 4.Floor Division ")
    ch=int(input("enter your choice "))
    if ch == 1:
        ob1+ob2

    elif ch == 2:
        ob1-ob2

    elif ch == 3:
        ob1*ob2

    elif ch == 4:
        ob1//ob2

    else:
        exit()