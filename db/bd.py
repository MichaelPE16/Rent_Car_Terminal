import sqlite3
from abc import ABC, abstractmethod


# here wer gonna call the first class related to the database management


class DATABASE: 
    """
    This modules is use to manage the data base over all inserting and read tables data
    """
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
    def insert_one(self, option):
        
            table = input('Which table u want to use ->')

            match table: 

                case 'user':
                    id_user = input('yout id ->') 
                    name = input("Your name ->")
                    lastname = input ('your lastname ->')
                    wallet = input("yout wallet amount ->")
                    email = input ('email ->')
                    user_password = input("Password ->")

                    with sqlite3.connect(self.path) as db: 
                        cursor = db.cursor()
                        cursor.execute(

                            f"insert into {table} values (?,?,?,?,?,?)",
                            (id_user, name, lastname, wallet, email, user_password),
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

                case 'car_rent': 
                    
                    id_carrent = input('Credentials id ->') 
                    user_id = input("user_id ->")
                    car_id = input ('car_id ->')
                    start = input("start date ->")
                    end = input('End date')

                    with sqlite3.connect(self.path) as db: 
                        cursor = db.cursor()
                        cursor.execute(

                                f"insert into {table} values (?,?,?,?,?)",
                            (id_carrent, user_id, car_id, start, end),
                        )

                case _: 
                    raise sqlite3.OperationalError("Table does not exists!!")
                
    def insert_many(self, lista : list):
        
        table = input('Which table u want to use ->')

        match table: 

            case 'user':
                
                with sqlite3.connect(self.path) as db: 
                    cursor = db.cursor()
                    cursor.executemany(

                        f"insert into {table} values (?,?,?,?,?,?)",
                        lista,
                    )

            case 'vehicles': 


                with sqlite3.connect(self.path) as db: 
                    cursor = db.cursor()
                    cursor.executemany(

                        f"insert into {table} values (?,?,?,?,?)",
                        lista,
                    )
                
            case 'car_rent': 
                

                with sqlite3.connect(self.path) as db: 
                    cursor = db.cursor()
                    cursor.execute(

                            f"insert into {table} values (?,?,?,?,?)",
                        lista,
                    )

            case _: 
                raise sqlite3.OperationalError("Table does not exists!!")


class MENU(ABC): 
    """This module contains the methods for the user, cars and all menus related
    """
    def __init__(self, path: str):
        self.path = path

    
    @abstractmethod
    def cars_menu(self):
        pass
    
    #make changes in wallet of user table
    @abstractmethod
    def make_payment(self): 
        pass
    @abstractmethod
    def user_menu(self):
        pass


class USER(MENU): 

    

    def __init__(self, path):
        super().__init__(path)
        self.autentificator = False
        

    def cars_menu(self):
        """Here the user can get access to the Vehicles Data"""
        if self.autentificator == True: 
            with sqlite3.connect(self.path) as db: 
                cursor = db.cursor()
                cursor.execute(
                """
                    SELECT * from vehicles
                """
                )
                vehicles =  cursor.fetchall()
            print("\nWELLCOME TO VEHICLES MENU!!\n")
            print(
                'OPTIONS-->\n',
                '1-SHOW ALL VEHICLES\n',
                '2-SHOW AVAILABLE VEHICLES\n',
                '3-SHOW UNAVAILABLE VEHICLES\n'
            )
            option = input("CHOOSE YOUR OPTION-->")
            match int(option): 
                case 1: 
                    print('\n ------------------------------ Vehicles Menu ----------------------------------------------------\n')
                    for i in vehicles: 
                        print(f' Vehicle ==> {i[1]} Model ==> {i[2]} Year ==> {i[3]} Price_rent ==> {i[4]} availability ==> {i[5]}\n')
                    print('-----------------------------------------------------------------------------------------------------')
               
                case 2: 
                    print('\n ------------------------------ Vehicles Menu ----------------------------------------------------\n')
                    for i in vehicles: 
                        if i[5] == True:
                            print(f' Vehicle ==> {i[1]} Model ==> {i[2]} Year ==> {i[3]} Price_rent ==> {i[4]} availability ==> {i[5]}\n')
                    print('-----------------------------------------------------------------------------------------------------')
                                
                case 3: 
                    print('\n ------------------------------ Vehicles Menu ----------------------------------------------------\n')
                    for i in vehicles: 
                        if i[5] == False:
                            print(f' Vehicle ==> {i[1]} Model ==> {i[2]} Year ==> {i[3]} Price_rent ==> {i[4]} availability ==> {i[5]}\n')
                    print('-----------------------------------------------------------------------------------------------------')

                case _: 
                    raise sqlite3.OperationalError('OPTION NOT AVAILABLE!!')
        else: 
            raise sqlite3.OperationalError("User not logged in")


    def make_payment(self):
        pass

    def user_menu(self):
       pass
    

    def autentification(self): 

        with sqlite3.connect(self.path) as db:
            cursor = db.cursor()
            cursor.execute(
                """
                select * from user
                """
            )
            users_data = cursor.fetchall()
        
        user_name = input('Loggin here -->')
        password = input('User_Password -->')

        for i in users_data: 
            
            if i[4] == user_name and i[5] == password: 
                self.autentificator = True
                
            
        
        if self.autentificator == True: 
            print('user loggin!!')
            

        else: 
                raise sqlite3.OperationalError("User Not Valid :(")




#Test
if __name__ == '__main__': 
    str_path = 'db/rentcar.db'
    database = DATABASE(str_path)
    # # lista = (
    # #     (3, "marlon", 'capardi', 16322.73),
    # #     (4, "Jairo", 'Seption', 16672.43),
    # #     (5, "Pedro", 'Logan', 19234.73),
    # # )
    # # database.insert_many(lista)
    # table = input("Which table to read ->")
    # data = database.read(table)
    # print(data)
    user1 = USER(str_path)
    try:
        user1.autentification()
        user1.cars_menu()

    except sqlite3.OperationalError as e:
        print(e)
    


    



    
    