from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserResponse(BaseModel):
    id: Optional[int]
    name: str = Field(min_length=3, max_length=64)
    email: EmailStr

    class Config:
        from_attributes = True
        populate_by_name = True
