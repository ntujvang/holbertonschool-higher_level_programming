-- Script that lists all shows contained in hbtn_0d_tvshows
-- In tv_shows.title - tv_shows_genres.genre_id format
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
JOIN tv_shows_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, genre_id ASC;
