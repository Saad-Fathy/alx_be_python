class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
        
class Library:
    def __init__(self):
        self._books = []
        
    def add_book(self,book):
        self._books.append(book)
        
    def list_available_books(self):
        # return [book for book in self._books if not book._is_checked_out]
        for book in self._books:
            if  not book._is_checked_out:
                print(f"{book.title} by {book.author}")
        
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
                    return f"Book {title} has been checked out"
                else:
                    return f"Book {title} is already checked out"
        return f"Book {title} not found in the library"
            
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    book._is_checked_out = False
                    return f"Book {title} has been returned"
        return f"Book {title} not found in the library"
            