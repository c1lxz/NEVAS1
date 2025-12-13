from typing import Annotated
from fastapi import Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession


from core.models.db import db_helper
from core.models.models_db.model import Module
from api_v1.modules import crud


async def module_by_id(
    module_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.get_scooped_session)
) -> Module:
    module = await crud.get_by_id(session=session, module_id=module_id)
    if module is not None:
        return module
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Module {module_id} not found!",
    )
    
    
    
async def module_by_course_id(
    course_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> list[Module]:
    modules = await crud.get_by_course_id(session=session, course_id=course_id)
    if modules is not None:
        return list(modules)
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Modules for the course with {course_id} ID not found"
    )