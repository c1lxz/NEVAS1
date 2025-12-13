from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db import db_helper
from api_v1.courses.schemas import Course
from api_v1.courses import crud
from api_v1.courses.dependencies import course_by_id


router = APIRouter(tags=["Courses"])


@router.get("/", response_model=list[Course])
async def get_courses(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_courses(session=session)

@router.get("/{course_id}/", response_model= Course) 
async def get_course(
    course: Course = Depends(course_by_id)
):
    return course

