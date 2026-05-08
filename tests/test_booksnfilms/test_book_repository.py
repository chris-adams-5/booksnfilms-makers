from lib.book_repository import BookRepository
from lib.book import Book

"""
Call album repository all and
return a list of book objects
which reflect the seed test data
"""

def test_book_repository_all(db_connection):
    db_connection.seed("seeds/booksnfilms.pgsql")
    repository = BookRepository(db_connection)
    books = repository.all()

    assert books == [
        Book(1,'The Gruffalo', 'Julia Donaldson', 'a beloved, award-winning rhyming picture book about a clever mouse navigating a deep, dark wood. To evade hungry predators—a fox, owl, and snake—the mouse invents a terrifying imaginary monster, the Gruffalo, only to come face-to-face with the real creature", "a rhyming bestseller about a curious young girl who embraces science to explore her world. When a terrible smell fills her home, Ada launches scientific experiments to find the source, learning to embrace failure and the power of asking "Why?". It is a STEM-focused tale celebrating curiosity and perseverance', 'https://media.johnlewiscontent.com/i/JohnLewis/109412271?fmt=auto&$background-off-white$&$rsp-pdp-port-640$'),
        Book(2,'Ada Twist, Scientist','Andrea Beaty', 'a rhyming bestseller about a curious young girl who embraces science to explore her world. When a terrible smell fills her home, Ada launches scientific experiments to find the source, learning to embrace failure and the power of asking "Why?". It is a STEM-focused tale celebrating curiosity and perseverance', 'https://img.fruugo.com/product/9/59/1869842599_max.jpg'),
        Book(3,'The Girl Who Drank the Moon', 'Kelly Barnhill', 'Every year, the people of the Protectorate leave a baby as an offering to the witch who lives in the forest. They hope this sacrifice will keep her from terrorizing their town. But the witch in the Forest, Xan, is in fact a good witch who shares her home with a wise Swamp Monster and a Perfectly Tiny Dragon. Xan rescues the children and delivers them to welcoming families on the other side of the forest, nourishing the babies with starlight on the journey.', 'https://m.media-amazon.com/images/I/61WUE9-GOHL._SY522_.jpg' ),
        Book(4, 'Dragons in a Bag', 'Zetta Elliott', 'When Jaxon is sent to spend the day with a mean old lady his mother calls Ma, he finds out she\'s not his grandmother--but she is a witch! She needs his help delivering baby dragons to a magical world where they\'ll be safe. There are two rules when it comes to the dragons: don\'t let them out of the bag, and don\'t feed them anything sweet. Before he knows it, Jax and his friends Vikram and Kavita have broken both rules! Will Jax get the baby dragons delivered safe and sound? Or will they be lost in Brooklyn forever?', 'https://m.media-amazon.com/images/I/8106dAeKbRL._SY522_.jpg')
    ]


"""
When I call find on BookRepository with an id
I get beck the corresponding book
"""

def test_book_repository_find(db_connection):
    db_connection.seed("seeds/booksnfilms.pgsql")
    repository = BookRepository(db_connection)
    book = repository.find(2)
    assert book == Book(2,'Ada Twist, Scientist','Andrea Beaty', 'a rhyming bestseller about a curious young girl who embraces science to explore her world. When a terrible smell fills her home, Ada launches scientific experiments to find the source, learning to embrace failure and the power of asking "Why?". It is a STEM-focused tale celebrating curiosity and perseverance', 'https://img.fruugo.com/product/9/59/1869842599_max.jpg')

"""
Create an entry for a book
"""

def test_book_repository_create(db_connection):
    db_connection.seed("seeds/booksnfilms.pgsql")
    repository = BookRepository(db_connection)
    new_book = Book(None, 'The Hitchhikers Guide to the Galaxy', "Douglas Adams", "A story that begins with a man", "url")
    result = repository.create(new_book)
    assert result == None
    books = repository.all()

    assert books == [
        Book(1,'The Gruffalo', 'Julia Donaldson', 'a beloved, award-winning rhyming picture book about a clever mouse navigating a deep, dark wood. To evade hungry predators—a fox, owl, and snake—the mouse invents a terrifying imaginary monster, the Gruffalo, only to come face-to-face with the real creature", "a rhyming bestseller about a curious young girl who embraces science to explore her world. When a terrible smell fills her home, Ada launches scientific experiments to find the source, learning to embrace failure and the power of asking "Why?". It is a STEM-focused tale celebrating curiosity and perseverance', 'https://media.johnlewiscontent.com/i/JohnLewis/109412271?fmt=auto&$background-off-white$&$rsp-pdp-port-640$'),
        Book(2,'Ada Twist, Scientist','Andrea Beaty', 'a rhyming bestseller about a curious young girl who embraces science to explore her world. When a terrible smell fills her home, Ada launches scientific experiments to find the source, learning to embrace failure and the power of asking "Why?". It is a STEM-focused tale celebrating curiosity and perseverance', 'https://img.fruugo.com/product/9/59/1869842599_max.jpg'),
        Book(3,'The Girl Who Drank the Moon', 'Kelly Barnhill', 'Every year, the people of the Protectorate leave a baby as an offering to the witch who lives in the forest. They hope this sacrifice will keep her from terrorizing their town. But the witch in the Forest, Xan, is in fact a good witch who shares her home with a wise Swamp Monster and a Perfectly Tiny Dragon. Xan rescues the children and delivers them to welcoming families on the other side of the forest, nourishing the babies with starlight on the journey.', 'https://m.media-amazon.com/images/I/61WUE9-GOHL._SY522_.jpg' ),
        Book(4, 'Dragons in a Bag', 'Zetta Elliott', 'When Jaxon is sent to spend the day with a mean old lady his mother calls Ma, he finds out she\'s not his grandmother--but she is a witch! She needs his help delivering baby dragons to a magical world where they\'ll be safe. There are two rules when it comes to the dragons: don\'t let them out of the bag, and don\'t feed them anything sweet. Before he knows it, Jax and his friends Vikram and Kavita have broken both rules! Will Jax get the baby dragons delivered safe and sound? Or will they be lost in Brooklyn forever?', 'https://m.media-amazon.com/images/I/8106dAeKbRL._SY522_.jpg'),
        Book(5, 'The Hitchhikers Guide to the Galaxy', "Douglas Adams", "A story that begins with a man", "url")
    ]

"""
Delete an entry from book_store
"""

def test_book_repository_delete(db_connection):
    db_connection.seed("seeds/booksnfilms.pgsql")
    repository = BookRepository(db_connection)
    result = repository.delete(3) # I apologise to no one
    assert result == None
    books = repository.all()

    assert books == [
        Book(1,'The Gruffalo', 'Julia Donaldson', 'a beloved, award-winning rhyming picture book about a clever mouse navigating a deep, dark wood. To evade hungry predators—a fox, owl, and snake—the mouse invents a terrifying imaginary monster, the Gruffalo, only to come face-to-face with the real creature", "a rhyming bestseller about a curious young girl who embraces science to explore her world. When a terrible smell fills her home, Ada launches scientific experiments to find the source, learning to embrace failure and the power of asking "Why?". It is a STEM-focused tale celebrating curiosity and perseverance', 'https://media.johnlewiscontent.com/i/JohnLewis/109412271?fmt=auto&$background-off-white$&$rsp-pdp-port-640$' ),
        Book(2,'Ada Twist, Scientist','Andrea Beaty', 'a rhyming bestseller about a curious young girl who embraces science to explore her world. When a terrible smell fills her home, Ada launches scientific experiments to find the source, learning to embrace failure and the power of asking "Why?". It is a STEM-focused tale celebrating curiosity and perseverance', 'https://img.fruugo.com/product/9/59/1869842599_max.jpg'),
        Book(4, 'Dragons in a Bag', 'Zetta Elliott', 'When Jaxon is sent to spend the day with a mean old lady his mother calls Ma, he finds out she\'s not his grandmother--but she is a witch! She needs his help delivering baby dragons to a magical world where they\'ll be safe. There are two rules when it comes to the dragons: don\'t let them out of the bag, and don\'t feed them anything sweet. Before he knows it, Jax and his friends Vikram and Kavita have broken both rules! Will Jax get the baby dragons delivered safe and sound? Or will they be lost in Brooklyn forever?', 'https://m.media-amazon.com/images/I/8106dAeKbRL._SY522_.jpg')
    ]