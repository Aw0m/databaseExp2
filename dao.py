import pymysql

db = pymysql.connect(host="localhost",
                     user="root",
                     password="",
                     database="db_project2",
                     port=3306)

cursor = db.cursor()


def select_staff(staff_id: int):
    try:
        cursor.execute("SELECT * FROM Staff WHERE staffID = %d;" % staff_id)
        data = cursor.fetchone()
        return data
    except:
        return "error"


def create_staff(staff_name: str, password: str, email: str, gender: str, age: int, phone: str, dep_id: int):
    try:
        cursor.execute(
            "INSERT INTO Staff (staffName, password, email, admin, gender, age, phone, depID) VALUES ('{}', '{}', '{}', 0, '{}', {:d}, '{}', {:d});".format(
                staff_name, password, email, gender, age, phone, dep_id))
        db.commit()
        return "ok"
    except Exception as e:
        print(e)
        db.rollback()
        return "error"


def delete_staff(staff_id: int):
    try:
        cursor.execute(
            "DELETE FROM staff WHERE staffID = %d" % staff_id
        )
        db.commit()
        return "ok"
    except Exception as e:
        db.rollback()
        print(e)
        return "error"


def update_staff(staff_id: int, staff_name: str, email: str, gender: str, age: int, phone: str,
                 dep_id: int):
    try:
        cursor.execute(
            "UPDATE staff SET staffName = '%s', email = '%s', gender = '%s',"
            " age = %d, phone = '%s', depID = '%d' WHERE staffID = '%d'" %
            (staff_name, email, gender, age, phone, dep_id, staff_id)
        )
        db.commit()
        return "ok"
    except Exception as e :
        db.rollback()
        print(e)
        return "error"
