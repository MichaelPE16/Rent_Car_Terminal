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
    def insert(self, option):
        
        if option.lower() == 'one': 
            table = input('Which table u want to use ->')

            match table: 
                case 'user':
                    id_user = input('yout id ->') 
                    name = input("Your name ->")
                    lastname = input ('your lastname ->')
                    wallet = input("yout wallet amount ->")

                    with sqlite3.connect(self.path) as db: 
                        cursor = db.cursor()
                        cursor.execute(

                            f"insert into {table} values (?,?,?,?)",
                            (id_user, name, lastname, wallet),
                        )



                case 'vehicles': 

                    id_vechicle = input('Vehicle id ->') 
                    name = input("Vehicle name ->")
                    model = input ('Vehicle model ->')
                    year = input("Vehicle year ->")
                    rent_price = input("Vehicle price")

                    with sqlite3.connect(self.path) as db: 
                        cursor = db.cursor()
                        cursor.execute(

                            f"insert into {table} values (?,?,?,?,?)",
                            (id_vechicle, name, model,year, rent_price),
                        )

                case 'credentials': 
                    pass
                case 'car_rent': 
                    pass 
                case _: 
                    raise sqlite3.OperationalError("Table does not exists!!")

        



        elif option.lower() == 'many': 
            pass
        else:
            raise sqlite3.OperationalError("\n Inser method not available \n")




#Test
if __name__ == '__main__': 
    str_path = 'db/rentcar.db'
    database = DATABASE(str_path)
    database.insert('oNe')
    table = input("Which table to read ->")
    data = database.read(table)
    print(data)
    
    