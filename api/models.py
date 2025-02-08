from typing import Optional
from pydantic import BaseModel, Field

class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, description="The name of the item")
    description: str = Field(..., min_length=1, description="The description of the item")

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: str = Field(..., description="The unique identifier of the item")