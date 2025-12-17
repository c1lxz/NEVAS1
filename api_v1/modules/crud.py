'''
Create
Read
Update
Delete
''' 

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from core.models.models_db.model import Module, Course
from api_v1.modules.schemas import ModuleCreate, ModuleUpdate, ModuleUpdatePartial



async def get_by_id(
    session: AsyncSession,
    module_id: int
) -> Module | None:
    return await session.get(Module, module_id)


async def get_by_course_id(
    session: AsyncSession,
    course_id: int
) -> list[Module]:
    stmt = select(Module).where(Module.course_id == course_id).order_by(Module.id)
    result: Result = await session.execute(stmt)
    modules = result.scalars().all()
    return list(modules)


async def create_module(
    session: AsyncSession,
    module_in: ModuleCreate
) -> Module:
    module = Module(**module_in.model_dump())
    session.add(module)
    await session.commit()
    return module


async def update_module(
    session: AsyncSession,
    module: Module,
    module_update: ModuleUpdate | ModuleUpdatePartial,
    partial: bool = False
) -> Module:
    data = module_update.model_dump(exclude_unset=partial)
    if "course_id" in data:
        course = await session.get(Course, data["course_id"])
        if not course:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail="Course not found"
            )
            
    for key, value in data.items():
        setattr(module, key, value)
        
    await session.commit()
    await session.refresh()
    return module


async def delete_module(
    session: AsyncSession,
    module: Module
) -> None:
    await session.delete(module)
    await session.commit()
    