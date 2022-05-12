from fastapi import FastAPI
import pymysql

db = pymysql.connect(host="localhost",
                     user="root",
                     password="lx2001812xx",
                     database="db_project2",
                     port=3306)


cursor = db.cursor()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
