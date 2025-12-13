from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db import db_helper
from api_v1.modules.schemas import Module
from api_v1.modules import crud
from api_v1.modules.dependencies import module_by_id, module_by_course_id


router = APIRouter(tags=["Modules"])


@router.get("/", response_model= list[Module])
async def get_modules(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_modules(session=session)


@router.get("/{module_id}/", response_model= Module)
async def get_module(
    module: Module = Depends(module_by_id)
):
    return module


@router.get("/{course_id}/modules/", response_model=list[Module])
async def get_modules_by_course_id(
    modules: list[Module] = Depends(module_by_course_id)
):
    return modules