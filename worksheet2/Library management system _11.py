class Library:
    def __init__(self):
        self.books=[]
    # Add books
    def add_book(self):
        book_id=int(input("enter book id: ")) 
        title=input("enter a title: ")
        author=input("enter a author: ")
        book={
            "id":book_id,
            "title":title,
            "author":author,
            "available":True
        }  
        self.books.append(book) 
        print("Book added successfully")
    #issued book
    def issue_book(self):
        book_id=int(input("enter a book id to issue: "))
        for book in self.books:
            if book["id"]==book_id:
                if book["available"]:
                    book["available"] = False
                    print("Book issued successfully")
                else:
                    print("Book is already issued")

                return
        print("Book not found") 

    #return book
    def return_book(self):
        book_id=int(input("enter a book id to return: "))
        for book in self.books:
            if book["id"]==book_id:
                if book["available"]:
                    book["available"] = True
                    print("Book return successfully")
                else:
                    print("Book is already return")

                return
        print("Book not found")    

    #display book
    def display_book(self):
        found = False 
        for book in self.books:
            if book["available"]:
                print(
                    "ID:", book["id"],
                    "Title:", book["title"],
                    "Author:", book["author"]
                )
                found = True                     
        if not found:
            print("No books available.")

library = Library()

# Menu
while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Available Books")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        library.add_book()

    elif choice == 2:
        library.issue_book()

    elif choice == 3:
        library.return_book()

    elif choice == 4:
        library.display_book()

    elif choice == 5:
        print("Thank you for using the Library Management System")
        break

    else:
        print("Invalid choice")






