from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db import db_helper
from api_v1.courses.schemas import Course, CourseCreate, CourseUpdate, CourseUpdatePartial
from api_v1.courses import crud
from api_v1.courses.dependencies import course_by_id


router = APIRouter(tags=["Courses"])


@router.get("/", response_model=list[Course])
async def get_courses(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_courses(session=session)



@router.post("/", response_model=Course, status_code=status.HTTP_201_CREATED)
async def create_course(
    course_in: CourseCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_course(session=session, course_in=course_in)


@router.get("/{course_id}/", response_model= Course) 
async def get_course(
    course: Course = Depends(course_by_id)
):
    return course


@router.put("/{course_id}/")
async def update_course(
    course_update: CourseUpdate,
    course: Course = Depends(course_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_course(
        session=session,
        course = course,
        course_update=course_update
    )
    
    
@router.patch("/{course_id}/")
async def update_course_partial(
    course_update: CourseUpdatePartial,
    course: Course = Depends(course_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_course(
        session=session,
        course=course,
        course_update=course_update,
        partial = True
    )


@router.delete("/{course_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(
    course: Course = Depends(course_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)    
) -> None:
    await crud.delete_course(session=session, course=course)

