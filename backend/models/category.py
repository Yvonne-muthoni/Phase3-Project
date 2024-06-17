from db import cursor,conn

class Category:
    TABLE_NAME = 'categories'

    def __init__(self,name):
        self.id = None
        self.name = name
    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (name)
        VALUES (?)
        """ 
        cursor.execute(sql,(self.name,)) 
        conn.commit()
        self.id= cursor.lastrowid
        print(f"{self.name} saved")
    def to_dict(self):
        return{
               "id":self.id,
               "name":self.name
            }
    @classmethod
    def find_all(cls):
        sql =f"""
            SELECT categories.* FROM categories
        """  
        rows = cursor.execute(sql).fetchall()
        return[
            cls.row_to_instance(row).to_dict() for row in rows

        ]
              
    @classmethod 
    def row_to_instance(cls,row):
        if row == None:
            return None
        categories = cls(row[1])
        categories.id = row[0]

        return categories

    @classmethod
    def create_table(cls):
        sql= f"""
           CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT NOT NULL

           )
        """    
        cursor.execute(sql)
        conn.commit()
        print(f"Categories table")
Category.create_table()
category_one = Category("cold")
category_one.save()        
#coffee.save()
#categories = ["hot","cold"]   

#for name in categories:
    #category = Category(name)
    #category.save()