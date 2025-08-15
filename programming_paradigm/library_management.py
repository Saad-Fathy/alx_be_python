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
        return self._books
    
    def check_out_book(self, title):
        if self._is_checked_out == False:
            return self._books
        else:
            self._books.remove(title)
            return self._books
