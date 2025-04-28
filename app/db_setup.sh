#! /bin/bash

# test, if file creates database and correctly inserts first five lines of csv file

# Delete movies.db 
rm movies.db

# Didn't add custom id column, as it breaks the import
# --skip 1 skips first row that contains titles
sqlite3 "movies.db" <<EOF
CREATE TABLE IF NOT EXISTS movies(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    tconst TEXT,
    primarytitle TEXT,
    startyear INTEGER,
    rank INTEGER ,
    averagerating REAL,
    numvotes INTEGER,
    runtimeminutes INTEGER,
    directors TEXT,
    writers TEXT,
    genres TEXT,
    imdblink TEXT,
    title_imdb_link TEXT
);

.mode csv
.import --skip 1 ./movies.csv movies

EOF
