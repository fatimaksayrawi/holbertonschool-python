-- Select with where.
SELECT t.name
FROM tv_genres t
LEFT JOIN (SELECT tv_genres.id
	FROM tv_genres
	JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
	JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_shows.title = 'Dexter') s1
ON t.id = s1.id
WHERE s1.id IS NULL
ORDER BY t.name ASC;
