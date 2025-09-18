#student library


class Library:
    def __init__(self,ListOfBooks):
        self.Books = ListOfBooks
    
    def DisplayAvailableBooks(self):
        print("Books present in this library are :")
        for Book in self.Books:
            print(" *" + Book)

    def BorrowBook(self,BookName):
        if BookName in self.Books:
            print(f"You have been issued {BookName} Book. keep it safe and return in 15 days..")
            self.Books.remove(BookName)
        else:
            print("Sorry This book is already taken. pls wait until the book is returned")
    
    def ReturnBook(self,BookName):
        self.Books.append(BookName)
        print("Thanks for returning this Book...!!!")



class Student:
    def RequestBook(self):
        self.book=input("Enter the name of book you want to borrow :")
        return self.book
    def ReturnBook(self):
        self.Book=input("Enter the name of Book you want to return :")
        return self.Book


if __name__=="__main__":
    CentralLibrary=Library(["Python","React","Django","Sql","Javascript"])
    student=Student()
    # CentralLibrary.DisplayAvailableBooks()

    while(True):
        WelcomeMsg='''--------------| Welcome to Library |--------------
        Please choose an option :
        1: Get list of all books.
        2: Request a book.
        3: Add/Return a book.
        4: Exit the library.
        '''
        print(WelcomeMsg)

        a= int(input("Enter a choice:"))
        if a==1:
            CentralLibrary.DisplayAvailableBooks()
        elif a==2:
            CentralLibrary.BorrowBook(student.RequestBook())
        elif a==3:
            CentralLibrary.ReturnBook(student.ReturnBook())
        elif a==4:
            print("thanks of choosing centralLibrary..!!! ")
            exit()
        else:
            print("Invalid choice..!!")