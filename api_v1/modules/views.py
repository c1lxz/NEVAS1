from fastapi import APIRouter, Depends,status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db import db_helper
from api_v1.modules.schemas import Module,ModuleCreate, ModuleUpdate, ModuleUpdatePartial
from api_v1.modules import crud
from api_v1.modules.dependencies import module_by_id, module_by_course_id


router = APIRouter(tags=["Modules"])


@router.get("/{module_id}/", response_model= Module)
async def get_module(
    module: Module = Depends(module_by_id)
):
    return module


@router.post("/", response_model=Module, status_code=status.HTTP_201_CREATED)
async def create_module(
    module_in: ModuleCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_module(session=session, module_in=module_in)


@router.get("/{course_id}/modules/", response_model=list[Module])
async def get_modules_by_course_id(
    modules: list[Module] = Depends(module_by_course_id)
):
    return modules


@router.put("/{module_id}/")
async def update_module(
    module_update: ModuleUpdate,
    module: Module = Depends(module_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_module(
        session=session,
        module=module,
        module_update=module_update
    )


@router.patch("/{module_id}/")
async def update_module_partial(
    module_update: ModuleUpdatePartial,
    module: Module = Depends(module_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_module(
        session=session,
        module = module,
        module_update=module_update,
        partial=True
    )
    
    
@router.delete("/{module_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    module: Module = Depends(module_by_id),
    session: AsyncSession = Depends(db_helper.get_scooped_session)    
) -> None:
    await crud.delete_module(session=session, module=module)
















