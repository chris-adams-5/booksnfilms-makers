from lib.book import Book

class BookRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM books")

        return [Book(row["id"],row["title"],row["author_name"],row["blurb"], row["image_url"]) for row in rows]
    
    def find(self, book_id):
        rows = self._connection.execute(
            'SELECT * FROM books WHERE id = %s', [book_id]
        )
        row = rows[0]
        return Book(row["id"],row["title"],row["author_name"],row["blurb"], row["image_url"])
    
    def create(self,new_book : Book):
        self._connection.execute('INSERT INTO books (title, author_name, blurb, image_url) VALUES (%s, %s, %s, %s)', [new_book.title, new_book.author_name, new_book.blurb, new_book.url])
        return None

    def delete(self, book_id):
        self._connection.execute('DELETE FROM books WHERE id = %s', [book_id])
        return None

    def __repr__(self):
        return 'BookRpository object'