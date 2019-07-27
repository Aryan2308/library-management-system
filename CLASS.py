class Books:
    def __init__(self, book_title='', book_author='', book_publication='', book_publication_year='', book_number=''):
        self.book_title = book_title
        self.book_author = book_author
        self.book_publication = book_publication
        self.book_publication_year = book_publication_year
        self.book_number = book_number
        
class Student(Books):
    def __init__(self, username = '', enrollment = '', admissionYear = '', semester = '', branch = '', issueBook = '', booknumber = '', fine = ''):
        self.username = username
        self.enrollment = enrollment
        self.admissionYear = admissionYear
        self.semester = semester
        self.branch = branch
        self.issueBook = 0
        self.booknumber = []
        self.fine = 0

class Faculty(Books):
    def __init__(self, facultyname = '', department = '' , fissueBook = '', fbooknumber = '', ffine = ''):
        self.facultyname = facultyname
        self.department = department
        self.fissueBook = 0
        self.fbooknumber = []
        self.ffine = 0