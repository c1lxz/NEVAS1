from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db import db_helper
from api_v1.lessons.schemas import Lesson, LessonCreate, LessonUpdate, LessonUpdatePartial
from api_v1.lessons import crud
from api_v1.lessons.dependencies import lesson_by_id, lessons_by_module_id

router = APIRouter(tags=["Lessons"])



@router.get("/{lessons_id}/", response_model= Lesson)
async def get_lesson(
    lesson: Lesson = Depends(lesson_by_id)
):
    return lesson


@router.post("/", response_model=Lesson, status_code=status.HTTP_201_CREATED)
async def create_lesson(
    lesson_in: LessonCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_lesson(session=session, lesson_in=lesson_in)


@router.get("/{module_id}/lessons/", response_model=list[Lesson])
async def get_lessons_by_module_id(
    lessons: list[Lesson] = Depends(lessons_by_module_id)
):
    return lessons


@router.put("/{lesson_id}/")
async def update_lesson(
    lesson_update: LessonUpdate,
    lesson: Lesson = Depends(lesson_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_lesson(
        session=session,
        lesson=lesson,
        lesson_update=lesson_update
    )


@router.patch("/{lesson_id}/")
async def update_lesson_partial(
    lesson_update: LessonUpdatePartial,
    lesson: Lesson = Depends(lesson_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_lesson(
        session=session,
        lesson=lesson,
        lesson_update=lesson_update,
        partial = True
    )


@router.delete("/{lesson_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lesson(
    lesson: Lesson = Depends(lesson_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    await crud.delete_lesson(session=session, lesson=lesson)