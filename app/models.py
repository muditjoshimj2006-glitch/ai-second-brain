from app.database import Base
from sqlalchemy import String, Integer, Column

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer,primary_key=True)

    name = Column(String,nullable=False)

    email = Column(
        String,
        unique=True,
        nullable=False,
        index=True
        )

    