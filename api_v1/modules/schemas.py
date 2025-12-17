from pydantic import BaseModel, ConfigDict

class ModuleBase(BaseModel):
    course_id: int
    title: str
    description: str
    
   
   
class ModuleCreate(ModuleBase):
    pass



class ModuleUpdate(ModuleCreate):
    pass 


class ModuleUpdatePartial(ModuleUpdate):
    course_id: int | None = None
    title: str | None = None
    description: str | None = None
    
class Module(ModuleBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int