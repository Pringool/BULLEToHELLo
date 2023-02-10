import sqlite3
import os

path_to_database = os.path.dirname(__file__) + "/data.sqlite3"
print(path_to_database)
con = sqlite3.connect(path_to_database)
cur = con.cursor()

class Database:
    def add_to_database(self, *args):
        if len(args) == 6:
            sql = "INSERT INTO Turtlegame(wave, score, name, playtime_begin, playtime_end, playtime) VALUES(?,?,?,?,?,?);"
            values = (args[0], args[1], args[2], args[3], args[4], args[5])
            cur.execute(sql, values)
            con.commit()
        
    
    
    def read_data(self):
        sql = "SELECT * FROM Turtlegame ORDER BY score ASC;"
        return cur.execute(sql)