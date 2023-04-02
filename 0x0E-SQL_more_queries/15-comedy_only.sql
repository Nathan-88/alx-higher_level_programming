-- Lists all comedy shows in the database hbtn_0d_tvshows.
-- Records are ordered by descending show title.
SELECT ts.title FROM tv_shows ts JOIN tv_show_genres tsg ON tsg.show_id = ts.id JOIN tv_genres tg ON tg.id = tsg.genre_id
JOIN tv_genres t ON t.id = tsg.genre_id WHERE t.name = 'Comedy' ORDER BY ts.title ASC;