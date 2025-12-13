'''
Create
Read
Update
Delete
'''

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.models_db import ContentBlock


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