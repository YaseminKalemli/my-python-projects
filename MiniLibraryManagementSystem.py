# Mini Library Management System

print("Welcome to the Mini Library Management System!")

library = {
    "python101": "Available",
    "datascience": "Available",
    "algorithms": "Available"
}
print("Current books in the library:")
for book, status in library.items():
    print(f"{book}: {status}")
    
borrowed_books = set()

while True:
    
    print("\nMenu Options:")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Exit")    

    choice = input("Please select an option (1-5): ") 
    if choice == "1":
         book = input("Enter the name of the book:").strip().lower()
         if book in library:
             print(f"{book} already exists!")
         else:
             library[book] = "Available"
             print(f"{book} is added to the library.")
             
    elif choice == "2":
        book = input("Enter the name of the book to borrow:").strip().lower()
        if book in library:
            library[book] = "Borrowed"
            borrowed_books.add(book)
            print(f"You have borrowed {book}.")
        else:
            print(f"{book} not found!")
            
    elif choice == "3":
        book = input("Enter the name of the book to return:").strip().lower()
        if library[book] == "Borrowed":
            library[book] = "Available"
            borrowed_books.remove(book)
            print(f"You have returned {book}.")
        else:
            print(f"{book} was not borrwed.")
            
    elif choice == "4":
        print("\nLibrary Books:")
        for book, status in library.items():
            print(f"{book.title()}:, {status}")
        print(f"Total books: {len(library)}")
        print(f"Borrowed books: {len(borrowed_books)}")
        
    elif choice == "5":
        print("Exiting the system... Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter number from 1 to 5.")
        
        
        
        
            
            
            
        
             
             
    
         
   
    

 
    

    

    
    
 
        
        
           
        
        
        
            
        
            
            
            
        
        
            
        
    

