from pydantic import BaseModel


class CourseBase(BaseModel):
    title: str
    description: str
    workload: int
    amount_of_exercises: int


class CourseRequest(CourseBase): ...


class CourseResponse(CourseBase):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True
