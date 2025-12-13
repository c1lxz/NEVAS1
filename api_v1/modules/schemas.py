from pydantic import BaseModel, ConfigDict

class ModuleBase(BaseModel):
    course_id: int
    title: str
    description: str
    
    
class Module(ModuleBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int