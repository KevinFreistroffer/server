from fastapi import APIRouter, HTTPException
from typing import Dict, List
from .storage import storage
from .models import Item, ItemCreate

router = APIRouter()

@router.get("/items", response_model=Dict[str, List[Item]])
async def get_items():
    """Get all items"""
    items = storage.get_all()
    return {'items': [Item(id=id, **data) for id, data in items.items()]}

@router.post("/items", response_model=Item, status_code=201)
async def create_item(item: ItemCreate):
    """Create a new item"""
    item_id, item_data = storage.create(item.dict())
    return Item(id=item_id, **item_data)

@router.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: str):
    """Get a specific item"""
    item = storage.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item(id=item_id, **item)

@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: ItemCreate):
    """Update a specific item"""
    updated_item = storage.update(item_id, item.model_dump())
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item(id=item_id, **updated_item)

@router.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: str):
    """Delete a specific item"""
    if not storage.delete(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return None