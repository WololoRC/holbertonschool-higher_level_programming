-- List all comedy shows
SELECT tv_shows.title FROM tv_shows INNER JOIN tv_show_genres tsg INNER JOIN tv_genres tg ON tg.id=tsg.genre_id AND tv_shows.id=tsg.show_id WHERE tg.name="Comedy" ORDER BY tv_shows.title;
