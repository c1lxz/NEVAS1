from pydantic import BaseModel, ConfigDict


class CourseBase(BaseModel):
    title: str
    description: str
    author: str
    image: str
    
    
    
class CourseCreate(CourseBase):
    pass


class CourseUpdate(CourseCreate):
    pass


class CourseUpdatePartial(CourseUpdate):
    title: str | None = None
    description: str | None = None
    author: str | None = None
    image: str | None = None
    
    
    
class Course(CourseBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int