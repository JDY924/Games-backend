/*
  1. Create table and figure out what values you want to store in the database

  2. Insert query that recognizes parameter variable

  3. Selecting all and some data from the database (2 calls)

  4. Update a specific entry in the database

  5. Delete a specific entry in the database
*/

CREATE TABLE games(
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  company TEXT NOT NULL
);
INSERT INTO games (ID, name, company) VALUES (?, ?, ?)
SELECT * FROM games;
SELECT name, company FROM games;

UPDATE games SET name = ?, company = ? WHERE ID = ?;

DELETE from games WHERE ID = ?;

