from typing import Annotated
from fastapi import Depends, FastAPI

from models.task import STaskAdd

app = FastAPI()

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