from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class TaskIn(BaseModel):
    title: str
    description: str
    is_done: bool = False


class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    user_id: int
    is_done: bool = Field(default=False)
    model_config = ConfigDict(from_attributes=True)

class TaskUpdate(BaseModel):
    title: str
    description: Optional[str] = None