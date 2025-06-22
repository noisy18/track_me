from typing import List
from database import TaskOrm, new_session
from schemas.task import STaskAdd, STask
from sqlalchemy import select

class TasksRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id


    @classmethod
    async def get_all(cls) -> List[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            data = await session.execute(query)
            task_models = data.scalars().all()
            tasks_schemas = [STask.model_validate(task_model) for task_model in task_models]
            return tasks_schemas