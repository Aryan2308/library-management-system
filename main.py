from Admin import *
from Student import *
from Faculty import *
import sys
def Menu():
    while True:
        print("Main Menu")
        print()
        print("*"*50)
        print("1.>  Admin Login")
        print("2.>  Student Login")
        print("3.>  Faculty Login")
        print("0.>  Exit\n")
        print("*" * 50)
        n = int(input("Enter Your Choice: "))
        if n==1:
            Admin_Menu()
        elif n==2:
            Student_Menu()
        elif n==3:
            Faculty_Menu()   
        elif n==0:
            sys.exit(0)
        else:
            print("Invalid Option")
Menu()