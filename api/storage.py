from typing import Dict, Optional
import uuid

class MemoryStorage:
    def __init__(self):
        self._storage: Dict[str, dict] = {}

    def get_all(self) -> Dict[str, dict]:
        return self._storage

    def get(self, item_id: str) -> Optional[dict]:
        return self._storage.get(item_id)

    def create(self, data: dict) -> tuple[str, dict]:
        item_id = str(uuid.uuid4())
        self._storage[item_id] = data
        return item_id, data

    def update(self, item_id: str, data: dict) -> Optional[dict]:
        if item_id in self._storage:
            self._storage[item_id] = data
            return data
        return None

    def delete(self, item_id: str) -> bool:
        if item_id in self._storage:
            del self._storage[item_id]
            return True
        return False

# Create a single instance for the application
storage = MemoryStorage()
