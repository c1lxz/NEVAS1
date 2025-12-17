from pydantic import BaseModel, ConfigDict

class ContentBlockBase(BaseModel):
    lesson_id: int
    type: str
    order: int
    content: str
    
    
class ContentBlockCreate(ContentBlockBase):
    pass 


class ContentBlockUpdate(ContentBlockCreate):
    pass


class ContentBlockUpdatePartial(ContentBlockUpdate):
    lesson_id: int |None = None
    type: str | None = None
    order: int | None = None
    content: str | None = None
    
    
class ContentBlock(ContentBlockBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int