-- 1. Название и год выхода альбомов, вышедших в 2018 году:

SELECT name, create_data FROM albums
WHERE create_data BETWEEN '01-01-2018' AND '31-12-2018';


-- 2. Название и продолжительность самого длительного трека:

SELECT name, duration FROM songs
ORDER BY duration DESC
LIMIT 1;


-- 3. Название треков, продолжительность которых не менее 3,5 минуты:

SELECT name FROM songs
WHERE duration > 3.5;


-- 4. Названия сборников, вышедших в период с 2018 по 2020 год включительно:

SELECT name FROM collections
WHERE create_data BETWEEN '01-01-2018' AND '31-12-2020';


-- 5. Исполнители, чье имя состоит из 1 слова:

SELECT * FROM performers
WHERE name NOT LIKE '% %'; 


-- 6. Название треков, которые содержат слово "мой"/"my":

SELECT name FROM songs
WHERE name LIKE '%my%'; 


-- 1. Количество исполнителей в каждом жанре:

SELECT g.name, COUNT(gp.performer_id) FROM genres AS g
JOIN performers_genres AS gp ON g.id = gp.genres_id
GROUP BY g.name
ORDER BY COUNT(gp.performer_id) DESC


-- 2. Количество треков, вошедших в альбомы 2019-2020 годов:

SELECT a.name, a.create_data, COUNT(s.id) FROM albums AS a
JOIN songs AS s ON a.id = s.album_id
WHERE a.create_data BETWEEN '01-01-2019' AND '31-12-2020'
GROUP BY a.name, a.create_data
ORDER BY a.create_data


-- 3. Средняя продолжительность треков по каждому альбому:

SELECT a.name, AVG(s.duration) FROM albums AS a
JOIN songs AS s ON a.id = s.album_id
GROUP BY a.name
ORDER BY AVG(s.duration) DESC


-- 4. Все исполнители, которые не выпустили альбомы в 2020 году:

SELECT p.name, p.surname FROM performers AS p
JOIN performers_albums AS pa ON p.id = pa.performer_id
JOIN albums AS a ON pa.album_id = a.id
WHERE create_data NOT BETWEEN '01-01-2020' AND '31-12-2020'


-- 5. Названия сборников, в которых присутствует конкретный исполнитель:

SELECT DISTINCT c.name, p.name, p.id, p.nickname FROM performers AS p
JOIN performers_albums AS pa ON p.id = pa.performer_id
JOIN albums AS a ON pa.album_id = a.id
JOIN songs AS s ON a.id = s.album_id
JOIN collection_songs AS cs ON s.id = cs.song_id
JOIN collections AS c ON cs.collection_id = c.id
WHERE p.nickname = 'lig'


-- 6. Название альбомов, в которых присутствуют исполнители более 1 жанра:

SELECT a.name FROM performers AS p
JOIN performers_albums AS pa ON p.id = pa.performer_id
JOIN albums AS a ON pa.album_id = a.id
JOIN performers_genres AS pg ON p.id = pg.performer_id
GROUP BY a.name
HAVING COUNT(pg.genres_id) > 1


-- 7. Наименование треков, которые не входят в сборники:

SELECT s.name FROM songs AS s
LEFT JOIN collection_songs AS cs ON s.id = cs.song_id
GROUP BY s.name, cs.song_id
HAVING cs.song_id IS NULL


-- 8. Исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть
-- несколько):

SELECT p.name, p.surname, s.duration FROM performers AS p
JOIN performers_albums AS pa ON p.id = pa.performer_id
JOIN albums AS a ON pa.album_id = a.id
JOIN songs AS s ON a.id = s.album_id
WHERE s.duration = (
	SELECT MIN(duration) FROM songs)


-- 9. Название альбомов, содержащих наименьшее количество треков:

SELECT a.name, COUNT(s.id) FROM albums AS a
JOIN songs AS s ON a.id = s.album_id
GROUP BY a.name
HAVING count(s.id) in (
    SELECT COUNT (s.id)
    FROM albums AS a
    JOIN songs AS s ON a.id = s.album_id
    GROUP BY a.name
    ORDER BY count(s.id)
    LIMIT 1)


