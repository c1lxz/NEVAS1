'''
Create
Read
Update
Delete
'''

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.models_db import Course



async def get_courses(
    session: AsyncSession
) -> list[Course]:
    stmt = select(Course).order_by(Course.id)
    result: Result = await session.execute(stmt)
    courses = result.scalars().all()
    return list(courses)


async def get_course(
    session: AsyncSession,
    course_id: int
) -> Course | None:
    return await session.get(Course, course_id)