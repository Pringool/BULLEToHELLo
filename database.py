import sqlite3
import sys


path_to_database = sys.path + "/data.sqlite3"
con = sqlite3.connect(path_to_database)
cur = con.cursor()

class Database:
    def add_to_database(self, *args):
        print(len(args))
    
    def read_data(self) -> str:
        pass