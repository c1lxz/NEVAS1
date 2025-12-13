from fastapi import APIRouter

from api_v1.modules.views import router as modules_router
from api_v1.lessons.views import router as lessons_router
from api_v1.courses.views import router as courses_router
from api_v1.content_blocks.views import router as content_blocks_router


router= APIRouter()
router.include_router(router=courses_router, prefix="/courses")
router.include_router(router=modules_router, prefix="/modules")
router.include_router(router=lessons_router, prefix="/lessons")
router.include_router(router=content_blocks_router, prefix="/content_blocks")
