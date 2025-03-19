import os
import json

# Load library from file if exists
def load_library():
    if os.path.exists("books.json"):
        with open("books.json", "r") as file:
            return json.load(file)
    else:
        return []

# Save library to a file
def save_library(library):
    with open("books.json", "w") as file:
        json.dump(library, file, indent=4)

# Add a book
def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = int(input("Enter publication year: "))
    genre = input("Enter book genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read_status": read_status
    }
    
    library.append(book)
    print(f"👍Book '{title}' added successfully!")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print(f"🧹 Book '{title}' removed successfully!")
            return
    print(f"Book with title '{title}' not found!")

# Search for a book
def search_book(library):
    search_query = input("🔎Enter title or author to search: ").lower()
    results = [book for book in library if search_query in book["title"].lower() or search_query in book["author"].lower()]
    
    if results:
        for book in results:
            print(f"{book['title']} by {book['author']} ({book['year']}, {book['genre']}) - {'Read' if book['read_status'] else 'Unread'}")
    else:
        print("No books found matching your search.")

# Display all books
def display_all_books(library):
    if not library:
        print("Your library is empty!")
        return
    for book in library:
        print(f"{book['title']} by {book['author']} ({book['year']}, {book['genre']}) - {'Read' if book['read_status'] else 'Unread'}")

# Display statistics
def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read_status"])
    unread_books = total_books - read_books
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    print(f"Total books: {total_books}")
    print(f"Books read: {read_books} ({percentage_read:.2f}% read)")
    print(f"Books unread: {unread_books}")

# Main menu
def main():
    library = load_library()
    
    while True:
        print("\nPersonal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("🫠 Enter your choice (1-6): ")
        
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_book(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(library)
            print("Library saved. 👋 Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
