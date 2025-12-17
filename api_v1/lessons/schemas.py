from pydantic import BaseModel, ConfigDict

class LessonBase(BaseModel):
    module_id: int
    title: str
    order: str
    description: str
    



class LessonCreate(LessonBase):
    pass 


class LessonUpdate(LessonCreate):
    pass


class LessonUpdatePartial(LessonUpdate):
    module_id: int | None = None
    title: str | None = None
    order: str | None = None
    description: str | None = None



class Lesson(LessonBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    