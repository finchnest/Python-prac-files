#main functions collection
class Library:
    def __init__(self, name, id_num, book=None,year=""):
        self.name = name
        self.id_num = id_num
        book = ["inorgnic chemistry","python","mathematics","chemistry","biology","physics"]
        if book is None:
            self.book = []
        else:
            self.book = book
    def display_info(self):
        print("User name:", self.name, " and ID:", self.id_num)
    def borrow(self, bk):
        if bk in self.book:
            print( bk ," is borrowed by ", self.name)
            self.book.remove(bk)
            print("Books available now are ")
            for z in self.book:
                print("-->",z)
        else:
            print("The book is not available! ")            
    def return_book(self, bk):
        if bk not in self.book:
            print("Thank you", self.name, "For returning the book ", bk)
            self.book.append(bk)
    def add_books(self, bk):
        if bk not in self.book:
            self.book.append(bk)
        print("Books available now are ")
        for j in self.book:
            print("-->",j)
    def remove_books(self, bk):
        if bk in self.book:
            self.book.remove(bk)
        print("Books available now are ")
        for j in self.book:
            print("-->",j)  
    def book_list(self):
        print("Books available in the library are ")
        for i in self.book:
            print("-->", i)
        return self.book
            
# Object classes     
class student(Library):
    def borr(self, bk):
        Library.borrow(self,bk)        
    def give_back(self, bk):
        Library.return_book(self,bk)

class teacher(Library):   
    def borr(self, bk):
        Library.borrow(self,bk)  
    def give_back(self, bk):
        Library.return_book(self,bk) 

class librarist(Library):
    def add(self, bk):
        Library.add_books(self,bk) 
    def remove(self, bk):
        Library.remove_books(self,bk)
    def show_books(self):
        Library.book_list(self,bk)

# For shell display           
def std(Name,ID):
        st1 = student(Name,ID)
        st1.display_info()  #we can do this because of inheritance
        st1.book_list()
        print("""1.Register for a course
2.See Grades""")
        x = eval(input("-->"))
        if x == 1:
            bk = str(input("Please write the book you want to borrow--> ")).lower()
            st1.borr(bk)
        elif x == 2:
            bk = str(input("Please write the book you want to return--> ")).lower()
            st1.give_back(bk)

def thr(Name,ID):
        teach1 = teacher(Name,ID)
        teach1.display_info()
        teach1.book_list()
        print("""1.Borrow a book
2.Return Book""")
        x = eval(input("-->"))
        if x == 1:
            bk = str(input("Please write the book you want to borrow--> ")).lower()
            teach1.borr(bk)
        elif x == 2:
            bk = str(input("Please write the book you want to return--> ")).lower()
            teach1.give_back(bk)
            
def lbst(Name,ID):
        libra = librarist(Name,ID)
        libra.display_info()
        print("""1.Add book
2.Remove book
3.View available books""")
        x = eval(input("-->"))
        if x == 1:
            bk = str(input("Write the name of the book to Add--> ")).lower()
            libra.add(bk)
        elif x == 2:
            bk = str(input("Write the name of the book to Remove--> ")).lower()
            libra.remove(bk)
        elif x==3:
            libra.book_list()

def check():
    print("""1.Teacher
2.Student
3.Registrar""")
    k = eval(input("-->"))
    if k == 1:
        Name = input("Your name: ")
        ID = input("Your ID-number: ")
        thr(Name,ID)
    elif k == 2:
        Name = input("Your name: ")
        ID = input("Your ID-number: ")
        std(Name,ID)
    elif k == 3:
        Name = input("Your name: ")
        ID = input("Your ID-number: ")
        lbst(Name,ID)            
check()
