from db import conn, cursor
from models.category import Category


class Product:
    TABLE_NAME="products"
    def __init__(self,title,desc,price,img):
        self.id = None
        self.title = title
        self.desc = desc
        self.price=price
        self.img = img

    def save(self):
        sql = f"""
            INSERT INTO{self.TABLE_NAME}(title,desc,price,img)
            VALUES(?,?,?,?)
        """
        cursor.execute(sql, (self.title,self.desc,self.price,self.img))  
        conn.commit()
        self.id = cursor.lastrowid

        return self

    def update(self):
        sql =f"""
                UPDATE{self.TABLE_NAME}
                SET title =?,desc =?,price =?,img=?
                WHERE id = ?
            """  
            cursor.execute(sql,(self.title,self.desc,self.pice,self.img))
            conn.commit()

            return self

    def to_dict (self):
            return{
                "id":self.id,
                "title":self.name
                "desc":self.desc
                "img":self.img
            }   
    @classmethod
    def find_one(cls, id):
        sql = """
            SELECT catalogues.*, genres.* FROM catalogues
            LEFT JOIN genres ON products.category_id = categories.id
            WHERE catalogues.id = ?
        """

        row = cursor.execute(sql, (id,)).fetchone()

        return cls.row_to_instance(row)
    @classmethod
    def find_all(cls):
        sql = """
            SELECT products.*, categories.* FROM products
            LEFT JOIN categories ON products.category_id = categories.id
            ORDER BY products.created_at ASC
        """

        rows = cursor.execute(sql).fetchall()

        return [
            cls.row_to_instance(row).to_dict() for row in rows
        ]
    @classmethod
    def find_all(cls):
        sql = """
            SELECT products.*, categories.* FROM products
            LEFT JOIN categories ON products.category_id = categories.id
            ORDER BY products.created_at ASC
        """

        rows = cursor.execute(sql).fetchall()

        return [
            cls.row_to_instance(row).to_dict() for row in rows
        ]
        
     @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                desc VARCHAR NOT NULL,
                img VARCHAR NOT NULL,
                price INTEGER NOT NULL,
    
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Products table created successfully")

Product.create_table()