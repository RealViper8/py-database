import os
import sqlite3
import configparser
import hashlib


try: import customtkinter; module = True
except ModuleNotFoundError:
    module = False

config = configparser.ConfigParser()



class database:
    def __init__(self,name,path : str | None="") -> None:
        if path == "":
            path = os.getcwd()
            print(path)
            os.system("pause")
        #try: 
            self.path = path
            self.name = name
            self.conn = sqlite3.connect(os.getcwd()+"\\"+self.name)
            self.c = self.conn.cursor()
        # except: print("Error: Directory not found"); os._exit(1)
    def add_table(self,table,var : list):
        var_str = str(var.copy())
        print(var_str)
        os.system("pause")
        self.c.execute("CREATE TABLE IF NOT EXISTS {}({})".format(table,var))
    def delete_table(self,table):
        pass

if __name__ == "__main__":
    os.system("title db")
    def again():
        try:
            config.read("config.ini")
        except: pass

        os.system("clear" if os.name == "posix" else "cls")
        os.system("color 0a")
        os.system("title db add")
        db = input("What database name -> ")
        path = input("Path (default current path) -> ")
        if not ".db" in db:
            db += ".db"
        if (path == "") or (path == "default") or (path == "Default") or (path.isspace()):
            path = os.getcwd()
        if (db == "" or db.isspace()):
            print("The database name shouldnt be empty  !\nPress enter to continiue")
            os.system("pause > nul")
            again()
        else:
            if not config.has_section("Database"): config.add_section("Database")
            config.set("Database","Name",db)
            config.set("Database","Path",path)
            with open("config.ini","w") as f:
                config.write(f)
    config.read("config.ini")
    if not config.has_section("Database"):
        again()
    count = 0
    while True:
        if count == 0:
            db = database(config.get("Database","Name"),config.get("Database","Path"))
            os.system("clear" if os.name == "posix" else "cls")
            os.system("title db "+config.get("Database","Name")+" & color 0a")
            print("\n### Type close to open another database ###\n")
            count += 1
        system = input("Database:{}$ ".format(config.get("Database","Path")))
        system_list = system.split(" ")
        if (system == "close") or (system == "Close"):
            again()
        elif (system == "ls") or (system == "list"):
            print()
            os.system("ls" if os.name == "posix" else "dir")
            print()
        elif (system == "cls") or (system == "clear"):
            os.system("clear" if os.name == "posix" else "cls")
        elif (system == "" or system.isspace()): print()
        elif (system_list != ""):
            try:
                system_list[0]
                if system_list[0] == "open":
                    system_list[1]
                    try:
                        config.set("Database","Name",system[1])
                        config.set("Database","Path",system[2])
                    except:
                        config.set("Database","Name",system[1])
                        config.set("Database","Path",os.getcwd())
                    with open("config.ini","w") as f:
                        config.write(f)
                else:
                    print(os.system(system_list))
            except:
                print("\nUsage of open :\n    open <Database_Name> <Path>\n")
        else:
            print()
            os.system(system)
            print()
        