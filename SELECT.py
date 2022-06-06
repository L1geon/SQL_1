import sqlalchemy

db = 'postgresql://postgres:admin@localhost:5432/music'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()


# 1. Название и год выхода альбомов, вышедших в 2018 году:

task_1_1 = connection.execute(
    """SELECT name, create_data FROM albums
    WHERE create_data BETWEEN '01-01-2018' AND '31-12-2018';"""
).fetchall()


# 2. Название и продолжительность самого длительного трека:

task_1_2 = connection.execute(
    """SELECT name, duration FROM songs
    ORDER BY duration DESC
    LIMIT 1;"""
).fetchall()


# 3. Название треков, продолжительность которых не менее 3,5 минуты:

task_1_3 = connection.execute(
    """SELECT name FROM songs
    WHERE duration > 3.5;"""
).fetchall()


# 4. Названия сборников, вышедших в период с 2018 по 2020 год включительно:

task_1_4 = connection.execute(
    """SELECT name FROM collections
    WHERE create_data BETWEEN '01-01-2018' AND '31-12-2020';"""
).fetchall()


# 5. Исполнители, чье имя состоит из 1 слова:

task_1_5 = connection.execute(
    """SELECT * FROM performers
    WHERE name NOT LIKE '%% %%';"""
).fetchall()


# 6. Название треков, которые содержат слово "мой"/"my":

task_1_6 = connection.execute(
    """SELECT name FROM songs
    WHERE name LIKE '%%my%%';"""
).fetchall()


# 1. Количество исполнителей в каждом жанре:

task_2_1 = connection.execute(
    """SELECT g.name, COUNT(gp.performer_id) FROM genres AS g
    JOIN performers_genres AS gp ON g.id = gp.genres_id
    GROUP BY g.name
    ORDER BY COUNT(gp.performer_id) DESC"""
).fetchall()


# 2. Количество треков, вошедших в альбомы 2019-2020 годов:

task_2_2 = connection.execute(
    """SELECT a.name, a.create_data, COUNT(s.id) FROM albums AS a
    JOIN songs AS s ON a.id = s.album_id
    WHERE a.create_data BETWEEN '01-01-2019' AND '31-12-2020'
    GROUP BY a.name, a.create_data
    ORDER BY a.create_data"""
).fetchall()


# 3. Средняя продолжительность треков по каждому альбому:

task_2_3 = connection.execute(
    """SELECT a.name, AVG(s.duration) FROM albums AS a
    JOIN songs AS s ON a.id = s.album_id
    GROUP BY a.name
    ORDER BY AVG(s.duration) DESC"""
).fetchall()


# 4. Все исполнители, которые не выпустили альбомы в 2020 году:

task_2_4 = connection.execute(
    """SELECT p.name, p.surname FROM performers AS p
    JOIN performers_albums AS pa ON p.id = pa.performer_id
    JOIN albums AS a ON pa.album_id = a.id
    WHERE create_data NOT BETWEEN '01-01-2020' AND '31-12-2020'"""
).fetchall()


# 5. Названия сборников, в которых присутствует конкретный исполнитель:

task_2_5 = connection.execute(
    """SELECT DISTINCT c.name, p.name, p.id, p.nickname FROM performers AS p
    JOIN performers_albums AS pa ON p.id = pa.performer_id
    JOIN albums AS a ON pa.album_id = a.id
    JOIN songs AS s ON a.id = s.album_id
    JOIN collection_songs AS cs ON s.id = cs.song_id
    JOIN collections AS c ON cs.collection_id = c.id
    WHERE p.nickname = 'lig'"""
).fetchall()


# 6. Название альбомов, в которых присутствуют исполнители более 1 жанра:

task_2_6 = connection.execute(
    """SELECT a.name FROM performers AS p
    JOIN performers_albums AS pa ON p.id = pa.performer_id
    JOIN albums AS a ON pa.album_id = a.id
    JOIN performers_genres AS pg ON p.id = pg.performer_id
    GROUP BY a.name
    HAVING COUNT(pg.genres_id) > 1"""
).fetchall()


# 7. Наименование треков, которые не входят в сборники:

task_2_7 = connection.execute(
    """SELECT s.name FROM songs AS s
    LEFT JOIN collection_songs AS cs ON s.id = cs.song_id
    GROUP BY s.name, cs.song_id
    HAVING cs.song_id IS NULL"""
).fetchall()


# 8. Исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть
# несколько):

task_2_8 = connection.execute(
    """SELECT p.name, p.surname, s.duration FROM performers AS p
    JOIN performers_albums AS pa ON p.id = pa.performer_id
    JOIN albums AS a ON pa.album_id = a.id
    JOIN songs AS s ON a.id = s.album_id
    WHERE s.duration = (
        SELECT MIN(duration) FROM songs)"""
).fetchall()


# 9. Название альбомов, содержащих наименьшее количество треков:

task_2_9 = connection.execute(
    """SELECT a.name, COUNT(s.id) FROM albums AS a
    JOIN songs AS s ON a.id = s.album_id
    GROUP BY a.name
    HAVING count(s.id) in (
        SELECT COUNT (s.id)
        FROM albums AS a
        JOIN songs AS s ON a.id = s.album_id
        GROUP BY a.name
        ORDER BY count(s.id)
        LIMIT 1)"""
).fetchall()
