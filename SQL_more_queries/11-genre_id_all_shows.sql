-- Select all shows and genres, if a show doesn't match with a genre there is gonna be a NULL.
SELECT ts.title, tsg.genre_id FROM tv_shows ts LEFT JOIN tv_show_genres tsg ON ts.id=tsg.show_id ORDER BY ts.title, tsg.genre_id;
