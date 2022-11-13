from conn import *


class crud:
    @staticmethod
    def find_all():
        conn = Connection.connection()
        try:
            cursor = conn.cursor()
            sql_exec = "select * from users"
            cursor.execute(sql_exec)
            return cursor.fetchall()
        except Exception:
            print('eoro')
        finally:
            conn.close()

    @staticmethod
    def find_by_id(id):
        conn = Connection.connection()
        try:
            cursor = conn.cursor()
            sql_exec = "select * from users where id=%s"
            cursor.execute(sql_exec, id)
            return cursor.fetchone()
        except Exception:
            print('eoro')
        finally:
            conn.close()

    @staticmethod
    def add(name, password):
        conn = Connection.connection()
        try:
            cursor = conn.cursor()
            sql_exec = "insert into users (login,password) values (%s,%s )"
            cursor.execute(sql_exec, (name, password))
            conn.commit()
            print("add ok")
        except Exception:
            print("rore")
        finally:
            conn.close()

    def delete_by_id(id):
        conn=Connection.connection()
        try:
            cursor = conn.cursor()
            sql_exec = "delete from users where id=%s;"
            cursor.execute(sql_exec, id)
            conn.commit()
            print("del ok")
        except Exception:
            print("h")
        finally:
            conn.close()



print(crud.find_all())
