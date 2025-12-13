from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db import db_helper
from api_v1.lessons.schemas import Lesson
from api_v1.lessons import crud
from api_v1.lessons.dependencies import lesson_by_id, lessons_by_module_id

router = APIRouter(tags=["Lessons"])


@router.get("/", response_model=list[Lesson])
async def get_lessons(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_lessons(session=session)


@router.get("/{lessons_id}/", response_model= Lesson)
async def get_lesson(
    lesson: Lesson = Depends(lesson_by_id)
):
    return lesson


@router.get("/{module_id}/lessons/", response_model=list[Lesson])
async def get_lessons_by_module_id(
    lessons: list[Lesson] = Depends(lessons_by_module_id)
):
    return lessons



