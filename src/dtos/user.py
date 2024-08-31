from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserResponse(BaseModel):
    id: Optional[int]
    name: str = Field(min_length=3, max_length=64)
    email: EmailStr

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
