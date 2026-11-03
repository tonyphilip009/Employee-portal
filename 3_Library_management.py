from mysql import  connector

class LibraryManagement:

    def __init__(self):
        try:
            self.connection=connector.connect(
                host="localhost",
                user="root",
                password="M7@vQ9#Lp2!Xr8$Zn5&K",
                database="library_db"
            )

            if self.connection.is_connected():
                print("connection successfully")
        except Exception as e:
            print(e)

    def get_a_book(self,id):

        try:

            cursor_connection=self.connection.cursor()

            query="select * from books where book_id=%s"

            value=(id,)

            cursor_connection.execute(query,value)

            get_the_value=cursor_connection.fetchone()

            if get_the_value is None:
                return None
            else:
                return get_the_value
        except Exception as e:
            print(e)

    def add_a_book(self,**kwarg):

        try:
            cursor_connection=self.connection.cursor()

            query="""insert into books(title,author,isbn,category,price,available_copies)
            values(%s,%s,%s,%s,%s,%s)"""

            values=[v for v in kwarg.values()]

            cursor_connection.execute(query,values)

            self.connection.commit()
            return "book details added successfully"
        except Exception as e:
            return e

    def get_all_books(self):

        try:
            cursro_connection=self.connection.cursor()

            query="""select * from books"""

            cursro_connection.execute(query)

            result=cursro_connection.fetchall()

            return result
        except Exception as e:
            return e

    def update_book_detials(self,id,**kwarg):

        result=self.get_a_book(id)

        try :
            if result!=None:
                cursor_connetion=self.connection.cursor()

                placeholder=""

                for key in kwarg.keys():
                    placeholder+=key+"=%s,"

                placeholder=placeholder.rstrip(",")

                query=f"""update books set {placeholder} where book_id=%s"""

                values=[v for v in kwarg.values()]

                values.append(id)

                cursor_connetion.execute(query,values)

                self.connection.commit()

                print("updated")
            else:
                raise ValueError("book doesn't exist")
        except Exception as e:
            print(e)

    def delete(self,id):

        try:
            cursor_connection=self.connection.cursor()

            query="""delete from books where book_id=%s"""

            value=(id,)

            cursor_connection.execute(query,value)

            self.connection.commit()

            print("deleted")
        except Exception as e:
            print(e)