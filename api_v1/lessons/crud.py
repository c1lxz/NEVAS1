'''
Create
Read
Update
Delete
'''

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.models_db.model import Lesson

async def get_lessons(
    session: AsyncSession
) -> list[Lesson]:
    stmt = select(Lesson).order_by(Lesson.id)
    result: Result = await session.execute(stmt)
    lessons = result.scalars().all()
    return list(lessons)


async def get_by_id(
    session: AsyncSession,
    lesson_id: int
) -> Lesson | None:
    return await session.get(Lesson, lesson_id)


async def get_by_module_id(
    session: AsyncSession,
    module_id: int
) -> list[Lesson]:
    stmt = select(Lesson).where(Lesson.module_id == module_id).order_by(Lesson.id)
    result: Result = await session.execute(stmt)
    lessons = result.scalars().all()
    return list(lessons)