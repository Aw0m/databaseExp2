from model import StaffInfo

from dao import select_staff, create_staff, delete_staff, update_staff
from utils import create_token


def login_service(staff_id: int, password: str) -> dict:
    try:
        data = select_staff(staff_id)
        if data[2] != password:
            return {"msg": "wrong password", "token": ""}

        token = create_token(staff_id, data[1])
        return {"msg": "ok", "token": token}
    except:
        return {"msg": "error", "token": ""}


def create_staff_service(creator_id: int, staff: StaffInfo):
    try:
        data = select_staff(creator_id)
        if not data[4]:
            # 权限不足 不是admin
            return {"msg": "not admin"}
        res = create_staff(staff.staffName, staff.password, staff.email,
                           staff.gender, staff.age, staff.phone, data[8])
        return {"msg": res}
    except:
        return {"msg": "error"}


def delete_staff_service(staff_id: int, manager_id: int):
    try:
        data = select_staff(manager_id)
        if not data[4]:
            # 权限不足 不是admin
            return {"msg": "not admin"}
        res = delete_staff(staff_id)
        return {"msg": res}
    except:
        return {"msg": "error"}


def select_staff_service(staff_id: int):
    try:
        data = select_staff(staff_id)
        return {
            "msg": "ok",
            "staffName": data[1],
            "email": data[3],
            "admin": data[4],
            "gender": data[5],
            "age": data[6],
            "phone": data[7],
            "depID": data[8]
        }
    except:
        return {
            "msg": "error",
            "staffName": None,
            "email": None,
            "admin": None,
            "gender": None,
            "age": None,
            "phone": None,
            "depID": None
        }


def update_staff_service(user_id: int, staff_id: int, staff: StaffInfo):
    try:
        data = select_staff(user_id)
        if not data[4]:
            # 权限不足 不是admin
            return {"msg": "not admin"}
        # res = create_staff(staff.staffName, staff.password, staff.email,
        #                    staff.gender, staff.age, staff.phone, data[8])
        res = update_staff(staff_id, staff.staffName, staff.email, staff.gender, staff.age, staff.phone, staff.dep_id)
        return {"msg": res}
    except:
        return {"msg": "error"}
