from pydantic import BaseModel, ConfigDict

class ContentBlockBase(BaseModel):
    lesson_id: int
    type: str
    order: int
    content: str
    
    
class ContentBlock(ContentBlockBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int