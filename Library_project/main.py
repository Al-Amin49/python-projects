from library import Library

def main():

    library = Library()

    while True:

        print("\n NEUB Library")

        print("1. Add Book")

        print("2. View Books")

        print("3. Borrow Book")

        print("4. Return Book")

        print("5. Exit")


        choice = input("Choose option: ").strip()


        if choice == "1":

            title = input("Enter title: ")

            author = input("Enter author: ")

            copies = input("Enter copies: ")


            print(library.add_book(title, author, copies))


        elif choice == "2":

            print(library.show_books())


        elif choice == "3":

            if library.has_books():

                print(library.show_books())

                book_number = input("Enter book number to borrow: ")

                print(library.borrow_book(book_number))

            else:

                print("No books available.")


        elif choice == "4":

            if library.has_books():

                print(library.show_books())

                book_number = input("Enter book number to return: ")

                print(library.return_book(book_number))

            else:

                print("No books available.")


        elif choice == "5":

            print("Goodbye!")
            break


        else:

            print("Invalid option.")

main()