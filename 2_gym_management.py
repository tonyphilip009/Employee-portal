from mysql import connector

class Database_connector:

    def get_connected(self):
        try:
            self.connection = connector.connect(
                host='localhost',
                user='root',
                password='M7@vQ9#Lp2!Xr8$Zn5&K',
                database='gym_db'
            )
            if self.connection.is_connected():
                print("Database connection successful")
            return self.connection
        except Exception as e:
            print(e)


class GymMemberManager(Database_connector):

    def get_object(self,id):
        try:
            connection=super().get_connected()
            cursor_obj=connection.cursor()

            query="""select * from member where id = %s"""
            value=(id,)

            cursor_obj.execute(query,value)
            result=cursor_obj.fetchone()

            return result
        except Exception as e:
            print(e)

    def get(self):
        try:
            connection = super().get_connected()
            cursor_object = connection.cursor()

            query = """select * from member"""

            cursor_object.execute(query)
            result = cursor_object.fetchall()

            for row in result:
                print(row)
        except Exception as e:
            print(e)

    def post(self, **kwargs):
        try:
            connection = super().get_connected()
            cursor_object = connection.cursor()

            query = """insert into member(name,place,mobile,plan,fee,joined_date)values(%s,%s,%s,%s,%s,%s)"""
            values = [v for v in kwargs.values()]

            cursor_object.execute(query, values)
            connection.commit()
            print("Member Detail added successfully")
        except Exception as e:
            print(e)

    def retrive(self, id=None):
        try:
            connection = super().get_connected()
            cursor_object = connection.cursor()

            query = """select * from member where id = %s"""
            value = (id,)

            cursor_object.execute(query, value)
            result = cursor_object.fetchone()
            print(result)
        except Exception as e:
            print(e)

    def delete(self, id):
        try:
            connection = super().get_connected()
            cursor_object = connection.cursor()

            query = """delete from member where id=%s"""
            value = (id,)

            cursor_object.execute(query, value)
            connection.commit()

            if cursor_object.rowcount > 0:
                print("deletion successful")
            else:
                print("there is no data with that id")
        except Exception as e:
            print(e)

    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record !=None:
                self.cursor=self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k+"=%s,"
                placeholder=placeholder.rstrip(",")
                query=f"update member set {placeholder} where id=%s"
                value=[v for v in kwargs.values()]
                value.append(id)
                self.cursor.execute(query,value)
                self.connection.commit()
                print("Member details updated successfully")
            else:
                print("member not found")
        except Exception as e:
            print(e)

member_object = GymMemberManager()
# member_object.get()
# member_object.post(name="Tony",place="kasaragod",mobile="9061568050",plan='3month',fee=5000,joined_date=datetime.datetime.today())
# member_object.post(name="Rahul",place="Kannur",mobile="9876543210",plan="1month",fee=1500,joined_date=datetime.datetime.today())
# member_object.post(name="Arjun",place="Payyannur",mobile="9123456780",plan="2month",fee=2800,joined_date=datetime.datetime.today())
# member_object.post(name="Vishnu",place="Taliparamba",mobile="9012345678",plan="3month",fee=4000,joined_date=datetime.datetime.today())
# member_object.retrive(id=3)
# member_object.delete(1)as
member_object.put(6,place="america")