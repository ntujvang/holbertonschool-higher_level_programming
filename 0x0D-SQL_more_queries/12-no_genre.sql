-- Script that lists all shows within hbtn_0d_tvshows without genre linked
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_shows_genres ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
