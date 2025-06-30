from pydantic import BaseModel, Field
from typing import Optional

class TaskIn(BaseModel):
    title: str
    description: str
    is_done: bool


class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    is_done: bool = Field(default=False)

class TaskUpdate(BaseModel):
    title: str
    description: Optional[str] = None