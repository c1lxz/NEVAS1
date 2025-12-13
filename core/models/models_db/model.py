from ast import Module
from sqlalchemy.orm import Mapped, relationship, mapped_column
from core.models.base import Base
from sqlalchemy import String, Text, CHAR, VARCHAR, ForeignKey, Integer


class Course(Base):
    __tablename__ = "courses"
    
    title: Mapped[str] = mapped_column(Text(100))
    description: Mapped[str] = mapped_column(Text)
    author: Mapped[str] = mapped_column(VARCHAR(52))
    image: Mapped[str] = mapped_column(String)
    modules: Mapped[list["Module"]] = relationship(back_populates="course")
    
    
    

class Module(Base): 
    __tablename__ = "modules"
    
    title: Mapped[str] = mapped_column(CHAR(100))
    description: Mapped[str] = mapped_column(Text)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    course: Mapped["Course"] = relationship(back_populates="modules")
    lessons: Mapped[list["Lesson"]] = relationship(back_populates="module")
    
    
    
class Lesson(Base):
    __tablename__ = "lessons"
    
    title: Mapped[str] = mapped_column(CHAR(100))
    order: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(Text)
    module_id: Mapped[int] = mapped_column(ForeignKey("modules.id"))
    module: Mapped["Module"] = relationship(back_populates="lessons")
    content_blocks: Mapped[list["ContentBlock"]] = relationship(back_populates="lesson")
    
    

class ContentBlock(Base):
    __tablename__ = "content_blocks"
    
    type: Mapped[str] = mapped_column(VARCHAR)
    order: Mapped[int] = mapped_column(Integer)
    content: Mapped[str] = mapped_column(Text)
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"))
    lesson: Mapped["Lesson"] = relationship(back_populates="content_blocks")
    
    
    