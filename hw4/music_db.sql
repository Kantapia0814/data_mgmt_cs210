-- Database Schema (60 pts)
-- 1.1 Artist
CREATE TABLE Artist (
    artist_name VARCHAR(64) PRIMARY KEY
);

-- 1.3 Album
CREATE TABLE Album (
    album_name VARCHAR(64) NOT NULL,
    album_artist VARCHAR(64) NOT NULL,
    album_date DATE NOT NULL,
    PRIMARY KEY (album_artist, album_name),
    FOREIGN KEY (album_artist) REFERENCES Artist(artist_name)
);

-- 1.2 Song
CREATE TABLE Genre (
    genre_name VARCHAR(64) PRIMARY KEY
); 

CREATE TABLE Song (
    song_name VARCHAR(64) NOT NULL,
    artist_name VARCHAR(64) NOT NULL,
    song_date DATE,
    album_name VARCHAR(64),
    album_artist VARCHAR(64),
    CHECK ((album_name IS NULL AND album_artist IS NULL)
        OR (album_name IS NOT NULL AND album_artist IS NOT NULL)),
    PRIMARY KEY (song_name, artist_name),
    FOREIGN KEY (artist_name) REFERENCES Artist(artist_name),
    FOREIGN KEY (album_artist, album_name) REFERENCES Album(album_artist, album_name)
);

CREATE TABLE SongandGenre (
    song_name VARCHAR(64) NOT NULL,
    song_artist VARCHAR(64) NOT NULL,
    genre_name VARCHAR(64) NOT NULL,
    PRIMARY KEY (song_name, song_artist, genre_name),
    FOREIGN KEY (song_name, song_artist) REFERENCES Song(song_name, artist_name),
    FOREIGN KEY (genre_name) REFERENCES Genre(genre_name)
);

-- 1.4 User
CREATE TABLE User (
    user_name VARCHAR(64) PRIMARY KEY
);

-- 1.5 Playlist
CREATE TABLE Playlist (
    playlist_title VARCHAR(64) NOT NULL,
    user_name VARCHAR(64) NOT NULL,
    playlist_time DATETIME NOT NULL,
    PRIMARY KEY (user_name, playlist_title),
    FOREIGN KEY (user_name) REFERENCES User(user_name)
);

CREATE TABLE PlaylistandSong (
    user_name VARCHAR(64) NOT NULL,
    playlist_title VARCHAR(64) NOT NULL,
    song_name VARCHAR(64) NOT NULL,
    song_artist VARCHAR(64) NOT NULL,
    PRIMARY KEY (user_name, playlist_title, song_name, song_artist),
    FOREIGN KEY (user_name, playlist_title) REFERENCES Playlist(user_name, playlist_title),
    FOREIGN KEY (song_name, song_artist) REFERENCES Song(song_name, artist_name)
);

-- 1.6 Rating
CREATE TABLE Rating (
    rating_id INT AUTO_INCREMENT PRIMARY KEY,
    rating_number TINYINT NOT NULL CHECK (rating_number IN (1, 2, 3, 4, 5)),
    rating_date DATE NOT NULL,
    user_name VARCHAR(64) NOT NULL,

    song_name VARCHAR(64),
    song_artist VARCHAR(64),
    album_artist VARCHAR(64),
    album_name VARCHAR(64),
    playlist_user VARCHAR(64),
    playlist_title VARCHAR(64),
    CHECK (((song_name IS NOT NULL AND song_artist IS NOT NULL)
        AND (album_name IS NULL AND album_artist IS NULL)
        AND (playlist_title IS NULL AND playlist_user IS NULL))
        OR ((album_name IS NOT NULL AND album_artist IS NOT NULL)
        AND (song_name IS NULL AND song_artist IS NULL)
        AND (playlist_title IS NULL AND playlist_user IS NULL))
        OR ((playlist_title IS NOT NULL AND playlist_user IS NOT NULL)
        AND (song_name IS NULL AND song_artist IS NULL)
        AND (album_name IS NULL AND album_artist IS NULL))),    
    FOREIGN KEY (user_name) REFERENCES User(user_name),
    FOREIGN KEY (song_name, song_artist) REFERENCES Song(song_name, artist_name),
    FOREIGN KEY (album_artist, album_name) REFERENCES Album(album_artist, album_name),
    FOREIGN KEY (playlist_user, playlist_title) REFERENCES Playlist(user_name, playlist_title)
);

-- Queries (60 points)
-- 2.1
SELECT
    genre_name AS genre,
    COUNT(*) AS number_of_songs
FROM 
    SongandGenre
GROUP BY 
    genre_name
ORDER BY 
    number_of_songs DESC
LIMIT 3;

-- 2.2
SELECT
    artist_name
FROM
    Song
GROUP BY
    artist_name
HAVING
    COUNT(IF(album_name IS NULL, 1, NULL)) > 0
    AND COUNT(IF(album_name IS NOT NULL, 1, NULL)) > 0;

-- 2.3
SELECT
    a.album_artist,
    a.album_name,
    AVG(rating_number) AS average_user_rating
FROM
    Album a
JOIN
    Rating r
    ON r.album_name = a.album_name
    AND r.album_artist = a.album_artist
WHERE
    r.rating_date BETWEEN '1990-01-01' AND '1999-12-31'
GROUP BY
    a.album_artist, a.album_name
ORDER BY
    average_user_rating DESC, 
    a.album_name ASC
LIMIT 10;

-- 2.4
SELECT
    sg.genre_name AS genre_name,
    COUNT(*) AS number_of_song_ratings
FROM
    Rating r
JOIN 
    SongandGenre sg 
    ON r.song_name = sg.song_name 
    AND r.song_artist = sg.song_artist
WHERE 
    r.rating_date BETWEEN '1991-01-01' AND '1995-12-31'
GROUP BY 
    sg.genre_name
ORDER BY 
    number_of_song_ratings DESC,
    sg.genre_name ASC
LIMIT 3;

-- 2.5
SELECT
    ps.user_name AS username,
    ps.playlist_title,
    AVG(song_avg.rating_number) AS average_song_rating
FROM
    PlaylistandSong ps
JOIN 
    (SELECT 
        r.song_name,
        r.song_artist,
        AVG(r.rating_number) AS rating_number
    FROM 
        Rating r
    JOIN Song s
    ON r.song_name = s.song_name AND r.song_artist = s.artist_name
    GROUP BY 
        r.song_name, r.song_artist
    ) AS song_avg
    ON ps.song_name = song_avg.song_name 
    AND ps.song_artist = song_avg.song_artist
GROUP BY 
    ps.user_name, ps.playlist_title
HAVING 
    AVG(song_avg.rating_number) >= 4.0;

-- 2.6
SELECT
    user_name AS username,
    COUNT(*) AS number_of_ratings
FROM 
    Rating
WHERE 
    (song_name IS NOT NULL AND song_artist IS NOT NULL)
    OR (album_name IS NOT NULL AND album_artist IS NOT NULL)
GROUP BY 
    user_name
ORDER BY 
    number_of_ratings DESC
LIMIT 5;

-- 2.7
SELECT
    s.artist_name,
    COUNT(*) AS number_of_songs
FROM 
    Song s
WHERE 
    s.song_date BETWEEN '1990-01-01' AND '2010-12-31'
GROUP BY 
    s.artist_name
ORDER BY 
    number_of_songs DESC
LIMIT 10;

-- 2.8
SELECT
    s.song_name AS song_title,
    COUNT(DISTINCT CONCAT(ps.user_name,'-',ps.playlist_title)) AS number_of_playlists
FROM 
    PlaylistandSong ps
JOIN Song s
    ON s.song_name = ps.song_name
    AND s.artist_name = ps.song_artist
GROUP BY 
    s.song_name, s.artist_name
ORDER BY 
    number_of_playlists DESC, 
    song_title ASC
LIMIT 10;

-- 2.9
SELECT
    r.song_name AS song_title,
    r.song_artist AS artist_name,
    COUNT(*) AS number_of_ratings
FROM 
    Rating r
JOIN 
    Song s 
    ON r.song_name = s.song_name 
    AND r.song_artist = s.artist_name
WHERE 
    s.album_name IS NULL
GROUP BY 
    r.song_name, r.song_artist
ORDER BY 
    number_of_ratings DESC, song_title ASC
LIMIT 20;

-- 2.10
SELECT 
    a.artist_name
FROM 
    Artist a
WHERE NOT EXISTS (
    SELECT 1
    FROM 
        Song s
    WHERE 
        s.artist_name = a.artist_name
        AND s.song_date > '1993-12-31'
);