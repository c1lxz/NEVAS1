from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db import db_helper
from api_v1.content_blocks.schemas import ContentBlock, ContentBlockCreate, ContentBlockUpdate, ContentBlockUpdatePartial
from api_v1.content_blocks import crud
from api_v1.content_blocks.dependencies import contentblock_by_id, contentblock_by_lesson_id

router = APIRouter(tags=["Content_blocks"])


@router.get("/{contentblock_id}/", response_model=ContentBlock)
async def get_contentblock(
    content_block: ContentBlock = Depends(contentblock_by_id)
):
    return content_block 


@router.post("/", response_model=ContentBlock, status_code=status.HTTP_201_CREATED)
async def create_content_block(
    content_block_in: ContentBlockCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> ContentBlock:
    return await crud.create_content_block(session=session, content_block_in=content_block_in)


@router.get("/{lesson_id}/content_blocks/", response_model=list[ContentBlock])
async def get_contentblocks(
    content_blocks: list[ContentBlock] = Depends(contentblock_by_lesson_id)
):
    return content_blocks


@router.put("/{content_block_id}/")
async def update_content_block(
    content_block_update: ContentBlockUpdate,
    content_block: ContentBlock = Depends(contentblock_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_content_block(
        session=session,
        content_block=content_block,
        content_block_update=content_block_update
    )
    
    
@router.patch("/{content_block_id}")
async def update_content_block_partial(
    content_block_update: ContentBlockUpdatePartial,
    content_block: ContentBlock = Depends(contentblock_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_content_block(
        session=session,
        content_block=content_block,
        content_block_update=content_block_update,
        partial = True
    )
    

@router.delete("/{content_block_id}")
async def delete_content_block(
    content_block: ContentBlock = Depends(contentblock_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    await crud.delete_content_block(session=session, content_block=content_block)
    