class Book:
    def __init__(self, id, title, author_name, blurb, url):
        self.id = id
        self.title = title
        self.author_name = author_name
        self.blurb = blurb
        self.url = url

    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.author_name}, {self.blurb}, {self.url})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__