from function import *
import sys
def Student_Menu():
    while True:
        print("Student Menu")
        print()
        print("*"*50)
        print("1.>  Display Book List")
        print("2.>  Search Book")
        print("3.>  Search Personal Records")
        print("0.>  Exit\n")
        print("*" * 50)
        n = int(input("Enter Your Choice: "))
        if n==1:
            displayBooks()
        elif n==2:
            bookSearch()
        elif n==3:
            studentSearch()   
        elif n==0:
            sys.exit(0)
        else:
            print("Invalid Option")
