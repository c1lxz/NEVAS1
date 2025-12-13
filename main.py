from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn


from core.models.models_db import Base, db_helper
from api_v1 import courses_router, modules_router, lessons_router, content_blocks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    
    
app = FastAPI(lifespan=lifespan)
app.include_router(courses_router, prefix="/courses")
app.include_router(modules_router, prefix="/modules")
app.include_router(lessons_router, prefix="/lessons")
app.include_router(content_blocks_router, prefix="/content_blocks")



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)