import sqlite3, csv
conn = sqlite3.connect("nba_sqlite.db")
cur = conn.cursor()

sql = """
    CREATE TABLE "nba_table" (
        ""	INTEGER NOT NULL UNIQUE,
        "Date"	REAL,
        "Start (ET)"	TEXT,
        "Visitor/Neutral"	TEXT,
        "PTS"	INTEGER,
        "Home/Neutral"	TEXT,
        "PTS.1"	INTEGER,
        "Unnamed: 6"	TEXT,
        "Unnamed: 7"	TEXT,
        "Attend."	INTEGER,
        "Notes"	TEXT,
        PRIMARY KEY("" AUTOINCREMENT)
    ) """

cur.execute(sql)
print("table has been created.")
conn.commit()
conn.close()