from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db import db_helper
from api_v1.content_blocks.schemas import ContentBlock
from api_v1.content_blocks import crud
from api_v1.content_blocks.dependencies import contentblock_by_id, contentblock_by_lesson_id

router = APIRouter(tags=["Content_blocks"])


@router.get("/", response_model=list[ContentBlock])
async def get_contentblocks(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_contentblocks(session=session)


@router.get("/{contentblock_id}/", response_model=ContentBlock)
async def get_contentblock(
    content_block: ContentBlock = Depends(contentblock_by_id)
):
    return content_block 


@router.get("/{lesson_id}/content_blocks/", response_model=list[ContentBlock])
async def get_contentblocks(
    content_blocks: list[ContentBlock] = Depends(contentblock_by_lesson_id)
):
    return content_blocks
