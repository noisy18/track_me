from typing import Annotated
from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI

from models.task import STaskAdd
from database import create_tabels, delete_tables

# Фукция для логгирования (удобно во время тестов, что база очищается при каждом тесте)
@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tabels()
    print("База готова к работе")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)

tasks = []

@app.post("/tasks")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
):
    tasks.append(task)
    return {"ok": True}






# @app.get("/tasks")
# def get_tasks():
#     task = Task(name="Соси")
#     return {"data": task}