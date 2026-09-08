from library import Book, EBook, Library, is_valid_isbn

def main():
    library = Library()

    book1 = Book("Harry Potter", 
                 "J.K. Rowling", 
                 "1234567890")
    book2 = Book("The Hobbit", 
                 "J.R.R. Tolkien", 
                 "2345678901")
    book3 = Book("1984", 
                 "George Orwell", 
                 "3456789012")
    
    ebook1 = EBook("Python Basics", 
                   "John Smith", 
                   "4567890123", 
                   5.5)
    ebook2 = EBook("Clean Code", 
                   "Robert Martin", 
                   "5678901234",
                     8.2)

  
    book4 = Book("The Metamorphosis", 
                 "Franz Kafka", 
                 "9999999991")
    book5 = Book("The Stranger", 
                 "Albert Camus", 
                 "9999999992")
    book6 = Book("Notes from Underground", 
                 "Fyodor Dostoevsky", 
                 "9999999993")
    
    ebook3 = EBook("And Then There Were None", 
                   "Agatha Christie", 
                   "9999999994", 
                   4.1)

    book7 = Book("Crime and Punishment", 
                 "Fyodor Dostoevsky", 
                 "8888888881")
    book8 = Book("The Trial", 
                 "Franz Kafka", 
                 "8888888882")
    book9 = Book("The Brothers Karamazov", 
                 "Fyodor Dostoevsky", 
                 "8888888883")

    # إضافة كل الكتب للمكتبة
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)
    library.add_book(book6)
    library.add_book(book7)
    library.add_book(book8)
    library.add_book(book9)
    library.add_book(ebook1)
    library.add_book(ebook2)
    library.add_book(ebook3)
    print("\n--- Checkout Book ---")
    library.checkout_book("1234567890") 
    library.checkout_book("8888888881") 

    print("\n--- Return Book ---")
    library.return_book("2345678901")

    print("\n--- Available Books (filter + lambda) ---")
    available_books = library.list_available_books()
    for book in available_books:
        print(book.describe())

    print("\n--- Sorted Books (sorted + lambda) ---")
    all_books = library.get_all_books()
    sorted_books = sorted(all_books, key=lambda book: book.title)
    for book in sorted_books:
        print(book.title)

    print("\n--- Book Titles (map + lambda) ---")
    titles = list(map(lambda book: book.title, all_books))
    for title in titles:
        print(title)

    print("\n--- Find Book ---")
    found_book = library.find_book("9999999991") 
    if found_book:
        print(found_book.describe())
    else:
        print("Book not found.")

if __name__ == "__main__":
    main()