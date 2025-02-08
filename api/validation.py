from typing import Tuple, Optional
from fastapi import Request

def validate_item(request: Request) -> Tuple[Optional[dict], Optional[str]]:
    """Validate item data from request"""
    try:
        data = request.json()
    except Exception:
        return None, "Invalid JSON data"

    if not isinstance(data, dict):
        return None, "Request body must be a JSON object"

    required_fields = ['name', 'description']
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return None, f"Missing required fields: {', '.join(missing_fields)}"

    if not isinstance(data.get('name'), str) or not isinstance(data.get('description'), str):
        return None, "name and description must be strings"

    if len(data.get('name', '')) < 1 or len(data.get('description', '')) < 1:
        return None, "name and description cannot be empty"

    return data, None