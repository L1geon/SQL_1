import sqlalchemy

db = 'postgresql://postgres:1203Csgo!12@localhost:5432/music'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

DLL_INSERT = connection.execute(
    """INSERT INTO performers(name, surname, nickname) VALUES
    ('Kirill', 'Piterov', 'lig'),
    ('Anton', 'Sminov', 'ads'),
    ('Denis', 'Antonov', 'dls'),
    ('Jim', 'Carrey','joker'),
    ('Brad', 'Pitt', 'liker'),
    ('Harry', 'Potter', 'pt'),
    ('Ron', 'Weasley', 'rw'),
    ('Hermione', 'Granger', 'HG');


    INSERT INTO albums(name, create_data) VALUES
    ('album1', '2005-01-01'),
    ('album2', '2010-01-01'),
    ('album3', '2015-01-01'),
    ('album4', '2018-01-01'),
    ('album5', '2018-02-01'),
    ('album6', '2018-03-01'),
    ('album7', '2019-01-01'),
    ('album8', '2020-01-01');


    INSERT INTO performers_albums VALUES
    (1, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 5),
    (3, 1),
    (6, 6),
    (7, 7),
    (8, 8);


    INSERT INTO songs(album_id, name, duration) VALUES
    (1, 'song1', 2),
    (2, 'song2', 5),
    (3, 'song3', 4),
    (4, 'song4', 6),
    (5, 'song5', 5),
    (6, 'song6', 4),
    (7, 'song7', 3),
    (8, 'song8', 5),
    (8, 'song9', 2),
    (7, 'song10', 3),
    (6, 'song11', 2),
    (5, 'song12', 3),
    (4, 'song13', 7),
    (3, 'song14', 5),
    (3, 'song15', 4),
    (3, 'song16', 2),
    (2, 'song17', 3),
    (1, 'song18', 4),
    (1, 'song19', 3);

INSERT INTO genres(name) VALUES
('Народная_музыка'),
('Академическая_музыка'),
('Фолк_музыка'),
('Латиноамериканская_музыка'),
('Блюз');

    INSERT INTO performers_genres VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 3),
    (7, 2),
    (8, 2);


    INSERT INTO collections(name, create_data) VALUES
    ('collection1', '2016-05-12'),
    ('collection2', '2018-03-03'),
    ('collection3', '2017-08-19'),
    ('collection4', '2018-03-12'),
    ('collection5', '2019-01-12'),
    ('collection6', '2020-03-12'),
    ('collection7', '2021-11-12'),
    ('collection8', '2022-03-12');


    INSERT INTO collection_songs VALUES
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 5),
    (8, 6),
    (5, 4),
    (2, 7),
    (3, 11),
    (1, 19),
    (2, 18),
    (3, 9),
    (5, 9),
    (3, 4),
    (6, 13),
    (4, 13),
    (1, 12),
    (1, 11),
    (8, 15),
    (6, 17);"""
)
