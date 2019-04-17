# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
songplay_table_create = ("""
    CREATE TABLE songplays(
    songplay_id SERIAL NOT NULL,
    start_time TIMESTAMP REFERENCES time(start_time),
    user_id VARCHAR(50) REFERENCES users(user_id),
    level VARCHAR(20),
    song_id VARCHAR(100) REFERENCES songs(song_id),
    artist_id VARCHAR(100) REFERENCES artists(artist_id),
    session_id INTEGER NOT NULL,
    location VARCHAR(255),
    user_agent TEXT,
    PRIMARY KEY (songplay_id))""")

user_table_create = ("""
    CREATE TABLE users(
    user_id VARCHAR NOT NULL,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    gender VARCHAR(3),
    level VARCHAR(20),
    PRIMARY KEY (user_id))""")

song_table_create = ("""
    CREATE TABLE songs(
    song_id VARCHAR(100) NOT NULL,
    title VARCHAR(255) NOT NULL,
    artist_id VARCHAR(100),
    year INTEGER,
    duration DOUBLE PRECISION,
    PRIMARY KEY (song_id))""")

artist_table_create = ("""
    CREATE TABLE artists(
    artist_id VARCHAR(100) NOT NULL,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    PRIMARY KEY (artist_id))""")

time_table_create = ("""
    CREATE TABLE time(
    start_time TIMESTAMP,
    hour INTEGER,
    day INTEGER,
    week INTEGER,
    month INTEGER,
    year INTEGER,
    weekday INTEGER,
    PRIMARY KEY (start_time))""")

# INSERT RECORDS
user_table_insert = ("""
    INSERT INTO users 
    (user_id, firstName, lastName, gender, level) 
    VALUES (%s, %s, %s, %s, %s) 
    ON CONFLICT (user_id) DO UPDATE SET 
    level=users.level """)

song_table_insert = ("""
    INSERT INTO songs 
    (song_id, title, artist_id, year, duration) 
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) 
    DO NOTHING;""")

artist_table_insert = ("""
    INSERT INTO artists 
    (artist_id, name, location, latitude, longitude) 
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) 
    DO NOTHING;""")

time_table_insert = ("""
    INSERT INTO time 
    (start_time, hour, day, week, month, year, weekday) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) 
    DO NOTHING;""")

songplay_table_insert = ("""
    INSERT INTO songplays 
    (start_time, user_id, level, song_id, artist_id, session_id, 
    location, user_agent) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """)

# FIND SONGS BY ARTIST ID
song_select_join = ("""
    SELECT s.song_id, a.artist_id FROM songs s, artists a
    WHERE s.artist_id = a.artist_id  
        AND s.title = %s
        AND a.name = %s
        AND s.duration = %s""")

# FIND USER BY ID
user_select = ("""
    SELECT COUNT(*) FROM users u
    WHERE u.user_id = %s""")

# FIND SONG BY ID
song_select = ("""
    SELECT COUNT(*) FROM songs s
    WHERE s.song_id = %s""")

# FIND ARTIST BY ID
artist_select = ("""
    SELECT COUNT(*) FROM artists a
    WHERE a.artist_id = %s""")

# QUERY LISTS
create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create,
                        songplay_table_create]
drop_table_queries = [user_table_drop, song_table_drop, artist_table_drop, time_table_drop,
                      songplay_table_drop]
