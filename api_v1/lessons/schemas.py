from pydantic import BaseModel, ConfigDict

class LessonBase(BaseModel):
    module_id: int
    title: str
    order: str
    description: str
    

class Lesson(LessonBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    