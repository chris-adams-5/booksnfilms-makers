class Film:
    def __init__(self, id, title, run_time_mins, director, imdb):
        self.id = id
        self.title = title
        self.run_time_mins = run_time_mins
        self.director = director
        self.imdb = imdb

    def __repr__(self) -> str:
        return f"Film({self.id}, {self.title}, {self.run_time_mins}, {self.director}, {self.imdb})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__