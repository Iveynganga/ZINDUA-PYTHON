class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def check_out(self):
        return "Checked out"
    
    def return_book(self):
        return "Not checked out"
    
    def __str__(self):
        return "title, author, isbn"
    
myBook = Book("Python", "Jack Doe", 2564)

print(myBook.title)
print(myBook.author)
print(myBook.isbn)
print(myBook.check_out())
print(myBook.return_book())
print(myBook.__str__())


class Library:
    def __init__(self):
        self.collection = []


    def add_book(self, book):
            if book not in self.collection:
                self.collection.append(book)
                print(f"Book '{book}'  was added to the library's collection.")

            else:       
                print(f"Book '{book}' already exists in the library's collection.")

    def remove_book(self, isbn):
        removed_book = None
        for book in self.collection:
            if book.isbn == isbn:
                removed_book = book
            if removed_book:
                 self.collection.remove(removed_book)
                 print(f"Book {removed_book} was removed from the library's collection")
            
            else:
                print("There is an error")

    def check_out_book(self, isbn):
        check_out_book = None
        for book in self.collection:
             if book.isbn ==isbn:
                checked_out_book = book
                if checked_out_book:
                    self.collection.remove(checked_out_book)
                    print(f"Book {checked_out_book} was checked out" )

        else:
            print("There is an error")

    def return_book(self,isbn):
        returned_book = Book("book found", "book checked out", isbn)
        if returned_book not in self.collection:
            self.collection.append(returned_book)
            print(f"Book with ISBN {isbn} is available" )

        else:
            print("There is an error")

    def list_books(self):
            if len(self.collection) ==0:
                    print("The library has no books in the collection.")
            else:
                print("The library has the following books: ")
                for book in self.collection:
                    print(book)
