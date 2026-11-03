from mysql import connector
import datetime


class Db_connection:

    def get_connected(self):

        try:
            connection = connector.connect(
                host="localhost",
                user='root',
                password='M7@vQ9#Lp2!Xr8$Zn5&K',
                database='company_db'
            )
            return connection
        except Exception as e:
            return print(e)


class EmployeeManager(Db_connection):

    def get_object(self, id):

        try:

            connection = super().get_connected()
            cursor_obj = connection.cursor()

            query = "select * from employee where id=%s"
            value = (id,)

            cursor_obj.execute(query, value)
            result = cursor_obj.fetchone()
            return result
        except Exception as e:
            print(e)

    def post(self, **kwargs):
        try:
            connection = super().get_connected()
            cursor_obj = connection.cursor()

            value = [v for v in kwargs.values()]
            query = """insert into employee(name,place,mobile,email,department,salary,joining_date)value(%s,%s,%s,%s,%s,%s,%s)"""

            cursor_obj.execute(query, value)
            connection.commit()
            print("employee details added successfully")
        except Exception as e:
            return print(e)

    def get(self):
        try:
            connection = super().get_connected()
            cursor_obj = connection.cursor()

            query = "select * from employee"

            cursor_obj.execute(query)
            result = cursor_obj.fetchall()

            for i in result:
                print(i)
        except Exception as e:
            print(e)

    def delete(self, id):
        try:
            connection = super().get_connected()
            cursor_obj = connection.cursor()

            query = "delete from employee where id=%s"
            value = (id,)

            cursor_obj.execute(query, value)
            connection.commit()

            if cursor_obj.rowcount > 0:
                print("employee is deleted")
            else:
                print("employee doesn't exist")
        except Exception as e:
            print(e)

    def put(self, id, **kwargs):

        try:
            result = self.get_object(id=id)

            if result != None:
                connnection = super().get_connected()
                cursor_obj = connnection.cursor()

                placeholder = ""

                for k in kwargs.keys():
                    placeholder += k + "=%s,"
                placeholder = placeholder.rstrip(",")
                query = f"update employee set {placeholder} where id=%s"
                value = [v for v in kwargs.values()]
                value.append(id)

                cursor_obj.execute(query, value)
                connnection.commit()
                print("employee details updated!")
            else:
                print("There is no employee with this id")
        except Exception as e:
            print(e)


class_object = EmployeeManager()
# class_object.post(name='tony',place='kasaragod',mobile=9061568050,email='tony@123',department='cse',salary=100000,joining_date=datetime.datetime.today())
# class_object.post(name='john',place='kochi',mobile=9876543210,email='john@123',department='hr',salary=75000,joining_date=datetime.datetime.today())
# class_object.post(name='rahul',place='kannur',mobile=9123456780,email='rahul@123',department='finance',salary=85000,joining_date=datetime.datetime.today())
# class_object.post(name='arun',place='calicut',mobile=9988776655,email='arun@123',department='marketing',salary=65000,joining_date=datetime.datetime.today())
# class_object.post(name='amal',place='trivandrum',mobile=9090909090,email='amal@123',department='it',salary=90000,joining_date=datetime.datetime.today())

# class_object.get()
# class_object.put(1,name='tyony',place='kyasyaragad')
class_object.delete(1)  
