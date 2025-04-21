import sqlite3


# here wer gonna call the first class related to the database management


class DATABASE: 
    def __init__(self, path: str):
        self.path = path

    #methods to use in data base

    #Read
    def read(self, table:str):
        with sqlite3.connect(self.path) as db:
            cursor = db.cursor()
            cursor.execute(

                f"select * from {table}"
            )
        return cursor.fetchall()

    # insert one




if __name__ == "__main__": 
    str_path = 'db/rentcar.db'
    database = DATABASE(str_path)
    table = input("Which table to read ->")
    data = database.read(table)
    print(data)

    