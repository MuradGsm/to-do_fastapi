from pydantic import BaseModel


class TaskIn(BaseModel):
    title: str
    description: str
    is_done: bool


class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    is_done: bool
