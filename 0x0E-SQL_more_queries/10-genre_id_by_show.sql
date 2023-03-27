-- Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
select tv_shows.title, tv_show_genres.genre_id from tv_shows join tv_show_genres ON tv_shows.id = tv_show_genres.show_id o
rder by tv_shows.title and tv_show_genres.genre_id;