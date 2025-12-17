'''
Create
Read
Update
Delete
'''

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from core.models.models_db import ContentBlock, Lesson
from api_v1.content_blocks.schemas import ContentBlockCreate, ContentBlockUpdatePartial, ContentBlockUpdate


async def get_contentblocks(
    session: AsyncSession
) -> list[ContentBlock]:
    stmt = select(ContentBlock).order_by(ContentBlock.id)
    result: Result = await session.execute(stmt)
    content_blocks = result.scalars().all()
    return list(content_blocks)


async def get_by_id(
    session: AsyncSession,
    contentblock_id: int
) -> ContentBlock | None:
    return await session.get(ContentBlock, contentblock_id)


async def get_by_lesson_id(
    session: AsyncSession,
    lesson_id: int
) -> list[ContentBlock]:
    stmt = select(ContentBlock).where(ContentBlock.lesson_id == lesson_id).order_by(ContentBlock.id)
    result: Result = await session.execute(stmt)
    content_blocks = result.scalars().all()
    return list(content_blocks)


async def create_content_block(
    session: AsyncSession,
    content_block_in: ContentBlockCreate
) -> ContentBlock:
    content_block = ContentBlock(**content_block_in.model_dump())
    session.add(content_block)
    await session.commit()
    return content_block


async def update_content_block(
    session: AsyncSession,
    content_block: ContentBlock,
    content_block_update: ContentBlockUpdate | ContentBlockUpdatePartial,
    partial: bool = False
) -> ContentBlock:
    data = content_block_update.model_dump(exclude_unset=partial)
    if "lesson_id" in data:
        lesson = await session.get(Lesson, data["lesson_id"])
        if not lesson:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Lesson not found"
            )
    for key, value in data.items():
        setattr(content_block, key, value)
        
    await session.commit()
    await session.refresh()
    return content_block


async def delete_content_block(
    session: AsyncSession,
    content_block: ContentBlock
) -> None:
    await session.delete(content_block)
    await session.commit()