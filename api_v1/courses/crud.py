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
from api_v1.courses.schemas import CourseCreate, CourseUpdate, CourseUpdatePartial


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


async def create_course(
    session: AsyncSession,
    course_in: CourseCreate
) -> Course:
    course = Course(**course_in.model_dump())
    session.add(course)
    await session.commit()
    return course


async def update_course(
    session: AsyncSession,
    course: Course,
    course_update: CourseUpdate | CourseUpdatePartial,
    partial: bool = False
) -> Course:
    for key, value in course_update.model_dump(exclude_unset=partial).items():
        setattr(course, key, value)
    await session.commit()
    return course


async def delete_course(
    session: AsyncSession,
    course: Course
) -> None:
    await session.delete(course)
    await session.commit()  
    
    
    
    