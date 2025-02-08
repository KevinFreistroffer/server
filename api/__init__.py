# Package initialization
from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Server",
    description="A FastAPI-based API server with in-memory storage",
    version="1.0.0"
)

# Import and setup routes
from .resources import router
app.include_router(router, prefix="/api", tags=["items"])

# Add OpenAPI documentation customization
app.openapi_tags = [
    {
        "name": "items",
        "description": "Operations with items in the storage",
    },
]