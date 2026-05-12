
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS films;
DROP TABLE IF EXISTS users;

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author_name VARCHAR(255),
    blurb TEXT,
    image_url TEXT
);

CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    title TEXT,
    run_time_minutes INT,
    director TEXT,
    imdb TEXT
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT
);


-- Books
INSERT INTO books (title, author_name, blurb, image_url) 
VALUES 
('The Gruffalo', 'Julia Donaldson', 'a beloved, award-winning rhyming picture book about a clever mouse navigating a deep, dark wood. To evade hungry predators—a fox, owl, and snake—the mouse invents a terrifying imaginary monster, the Gruffalo, only to come face-to-face with the real creature", "a rhyming bestseller about a curious young girl who embraces science to explore her world. When a terrible smell fills her home, Ada launches scientific experiments to find the source, learning to embrace failure and the power of asking "Why?". It is a STEM-focused tale celebrating curiosity and perseverance', 'https://media.johnlewiscontent.com/i/JohnLewis/109412271?fmt=auto&$background-off-white$&$rsp-pdp-port-640$'),

('Ada Twist, Scientist','Andrea Beaty', 'a rhyming bestseller about a curious young girl who embraces science to explore her world. When a terrible smell fills her home, Ada launches scientific experiments to find the source, learning to embrace failure and the power of asking "Why?". It is a STEM-focused tale celebrating curiosity and perseverance', 'https://img.fruugo.com/product/9/59/1869842599_max.jpg'),

('The Girl Who Drank the Moon', 'Kelly Barnhill', 'Every year, the people of the Protectorate leave a baby as an offering to the witch who lives in the forest. They hope this sacrifice will keep her from terrorizing their town. But the witch in the Forest, Xan, is in fact a good witch who shares her home with a wise Swamp Monster and a Perfectly Tiny Dragon. Xan rescues the children and delivers them to welcoming families on the other side of the forest, nourishing the babies with starlight on the journey.' , 'https://m.media-amazon.com/images/I/61WUE9-GOHL._SY522_.jpg' ),

('Dragons in a Bag', 'Zetta Elliott', 'When Jaxon is sent to spend the day with a mean old lady his mother calls Ma, he finds out she''s not his grandmother--but she is a witch! She needs his help delivering baby dragons to a magical world where they''ll be safe. There are two rules when it comes to the dragons: don''t let them out of the bag, and don''t feed them anything sweet. Before he knows it, Jax and his friends Vikram and Kavita have broken both rules! Will Jax get the baby dragons delivered safe and sound? Or will they be lost in Brooklyn forever?', 'https://m.media-amazon.com/images/I/8106dAeKbRL._SY522_.jpg');


INSERT INTO films (title, run_time_minutes, director, imdb)
VALUES
('Jurassic Park', 122, 'Steven Spielberg', 'https://www.imdb.com/title/tt0107290/'),
('Snakes on a Plane', 105, 'David R Ellis', 'https://www.imdb.com/title/tt0417148/'),
('Snakes on a Train', 91, 'Peter Mervis', 'https://www.imdb.com/title/tt0843873/');

INSERT INTO users (username, password)
VALUES
('user', 'password'),
('speckled_jim','meeeh');