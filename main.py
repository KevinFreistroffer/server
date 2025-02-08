import logging
import uvicorn
from api import app

# Configure logging with more detail
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    uvicorn.run("api:app", host="localhost", port=5000, log_level="debug")