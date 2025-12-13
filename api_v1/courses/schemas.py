from pydantic import BaseModel, ConfigDict


class CourseBase(BaseModel):
    title: str
    description: str
    author: str
    image: str
    
    
    
class Course(CourseBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int