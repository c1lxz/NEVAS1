'''
Create
Read
Update
Delete
''' 

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.models_db.model import Module


async def get_modules(
    session: AsyncSession
) -> list[Module]:
    stmt = select(Module).order_by(Module.id)
    result: Result = await session.execute(stmt)
    modules = result.scalars().all()
    return list(modules)


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