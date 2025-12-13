from typing import Annotated
from fastapi import Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession


from core.models.db import db_helper
from core.models.models_db.model import Lesson
from api_v1.lessons import crud


async def lesson_by_id(
    lesson_id: Annotated[int, Path],
    session = Depends(db_helper.scoped_session_dependency)
) -> Lesson:
    lesson = await crud.get_by_id(session=session, lesson_id=lesson_id)
    if lesson is not None:
        return lesson
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Lesson {lesson_id} not found",
    )
    
    
async def lessons_by_module_id(
    module_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> list[Lesson]:
    lessons = await crud.get_by_module_id(session=session, module_id=module_id)
    if lessons is not None:
        return list(lessons) 
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Lessons for the module with {module_id} ID not found",
    )   