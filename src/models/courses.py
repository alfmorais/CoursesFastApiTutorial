from sqlalchemy import Column, Integer, String

from src.config.database import Base


class Course(Base):
    __tablename__ = "courses"

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String(100), nullable=False)
    description: str = Column(String(255), nullable=False)
    workload: int = Column(Integer, nullable=False)
    amount_of_exercises: int = Column(Integer, nullable=False)
