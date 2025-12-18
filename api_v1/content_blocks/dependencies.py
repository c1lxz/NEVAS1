from typing import Annotated
from fastapi import Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession


from core.models.db import db_helper
from core.models.models_db.model import ContentBlock, Lesson
from api_v1.content_blocks import crud


async def contentblock_by_id(
    contentblock_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> ContentBlock:
    contentblock = await crud.get_by_id(session=session, contentblock_id=contentblock_id)
    if contentblock is not None:
        return contentblock
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Content {contentblock_id} not found",
    )
    
    
async def contentblock_by_lesson_id(
    lesson_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> list[ContentBlock]:
    lesson = await session.get(Lesson, lesson_id)
    if not lesson:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lesson {lesson_id} not found"
        )
        
    content_blocks = await crud.get_by_lesson_id(session=session, lesson_id=lesson_id)
    if not content_blocks:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Content_blocks for the lesson with {lesson_id} ID not found",
        )
    return list(content_blocks)