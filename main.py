from fastapi import FastAPI
from service import *
from utils import verify_token
from model import *

app = FastAPI()


@app.post("/api/login")
async def login(item: LoginItem):
    """
    用户登陆
    :param item:
    :return:
    """
    return login_service(item.staff_id, item.password)


@app.post("/api/staff")
async def create_staff(token: Token, staff: StaffInfo):
    """
    创建用户
    :param token:
    :param staff:
    :return:
    """
    staff_id, _ = verify_token(token.access_token)
    if staff_id == -1:
        return {"msg": "wrong token"}
    return create_staff_service(staff_id, staff)


@app.get("/api/staff")
async def get_staff(token: str, staff_id: int):
    """
    查询用户
    :param token:
    :param staff_id:
    :return:
    """
    user_id, _ = verify_token(token)
    if user_id == -1:
        return {"msg": "wrong token"}
    return select_staff_service(staff_id)


@app.delete("/api/staff/")
async def delete_staff(token: Token, staff_id: StaffID):
    """
    删除用户
    :param token:
    :param staff_id:
    :return:
    """
    manager_id, _ = verify_token(token.access_token)
    if staff_id == -1:
        return {"msg": "wrong token"}
    return delete_staff_service(staff_id.staff_id, manager_id)




@app.put("/api/staff/{staff_id}")
async def update_staff(token: Token, staff: StaffInfo, staff_id: int):
    user_id, _ = verify_token(token.access_token)
    if user_id == -1:
        return {"msg": "wrong token"}
    return update_staff_service(user_id, staff_id, staff)

