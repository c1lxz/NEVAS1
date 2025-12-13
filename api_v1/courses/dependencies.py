from typing import Annotated
from fastapi import Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession


from core.models.db import db_helper
from core.models.models_db import Course
from api_v1.courses import crud

async def course_by_id(
    course_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Course:
    course = await crud.get_course(session=session, course_id=course_id)
    if course is not None:
        return course
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Course {course_id} not found!",
    )
    
    