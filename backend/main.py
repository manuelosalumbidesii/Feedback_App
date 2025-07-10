from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict
import logging


app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# CORS settings (open for dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic model for input validation
class Feedback(BaseModel):
    name: str
    message: str


# Optional: health check endpoint
@app.get("/")
async def root() -> Dict[str, str]:
    return {"status": "OK", "message": "Feedback API is running"}


# POST endpoint to receive feedback
@app.post("/feedback", response_model=Dict[str, str])
async def receive_feedback(feedback: Feedback) -> Dict[str, str]:
    logger.info(
        f"📩 Feedback received from {feedback.name}: {feedback.message}"
    )
    return {"message": f"Thank you, {feedback.name}! Feedback received."}
