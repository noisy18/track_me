from contextlib import asynccontextmanager
from fastapi import FastAPI

from database import create_tabels, delete_tables
from router import router as tasks_router

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
app.include_router(tasks_router)