CREATE table a20506653.music(
artistname text,
albumname text,
numbersold int,
cost int,
PRIMARY KEY(artistname, albumname)
) WITH CLUSTERING ORDER BY (albumname DESC);
