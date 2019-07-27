from function import *
import sys
def Admin_Menu():
    while True:
        print("*"*50)
        print("1.>  Insert Book")
        print("2.>  Display Book List")
        print("3.>  Book Search")
        print("4.>  Book Issue for Student")
        print("5.>  Book Issue for Faculty")
        print("6.>  Book Return of Student")
        print("4.>  Book Return of Faculty")
        print("8.>  Delete Book Record")
        print("9.>  Insert New Student")
        print("10.> Display Student List")
        print("11.> Student Search")
        print("12.> Delete Student Record")
        print("13.> Insert New Faculty")
        print("14.> Display Faculty")
        print("15.> Faculty Search")
        print("16.> Delete Faculty")
        print("0> Exit\n")
        print("*" * 50)
        n = int(input("Enter Your Choice: "))
        if n==1:
            bookStore()
        elif n==2:
            displayBooks()
        elif n==3:
            bookSearch()
        elif n==4:
            student_bookIssue()
        elif n==5:
            faculty_bookIssue()
        elif n==6:
            s_bookReturn()
        elif n==7:
            f_bookReturn()
        elif n==8:    
            bookDelete()
        elif n==9:
            inputStudent()
        elif n==10:
            displayStudent()
        elif n==11:
            studentSearch()
        elif n==12:
            studentDelete()
        elif n==13:
            inputFaculty()
        elif n==14:
            displayFaculty()
        elif n==15:
            facultySearch()
        elif n==16:
            facultyDelete()    
        elif n==0:
            sys.exit(0)
        else:
            print("Invalid Option")