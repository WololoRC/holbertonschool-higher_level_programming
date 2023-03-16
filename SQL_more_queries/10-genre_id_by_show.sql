-- List all shows contained in hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows, tv_show_genres WHERE tv_shows.id=show_id ORDER BY title, genre_id ASC;
