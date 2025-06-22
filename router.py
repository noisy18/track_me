from fastapi import APIRouter
from typing import Annotated, List
from fastapi import Depends

from schemas.task import STaskAdd, STask, STaskId
from repositories.task import TasksRepository

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"]
)

tasks = []
repo = TasksRepository()

@router.post("/add")
async def post(
    task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await repo.add_one(task)
    return {"status": True, "task_id": task_id}

@router.get("/get")
async def get() -> List[STask]:
    tasks = await repo.get_all()
    return {"data": tasks}