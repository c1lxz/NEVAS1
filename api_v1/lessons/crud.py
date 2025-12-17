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

from core.models.models_db.model import Lesson, Module
from api_v1.lessons.schemas import LessonCreate, LessonUpdate, LessonUpdatePartial



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


async def create_lesson(
    session: AsyncSession,
    lesson_in: LessonCreate
) -> Lesson:
    lesson = Lesson(**lesson_in.model_dump())
    session.add(lesson)
    await session.commit()
    return lesson


async def update_lesson(
    session: AsyncSession,
    lesson: Lesson,
    lesson_update: LessonUpdate | LessonUpdatePartial,
    partial: bool = False
) -> Lesson:
    data = lesson_update.model_dump(exclude_unset=partial)
    if "module_id" in data:
        module = await session.get(Module, ["module_id"])
        if not module:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Module not found"
            )
    for key, value in data.items():
        setattr(Lesson, key, value)
    
    await session.commit()
    await session.refresh()
    return lesson


async def delete_lesson(
    session: AsyncSession,
    lesson: Lesson
) -> None:
    await session.delete(lesson)
    await session.commit()