from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow requests from frontend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for validation
class Feedback(BaseModel):
    name: str
    message: str

# POST endpoint to receive feedback
@app.post("/feedback")
async def receive_feedback(feedback: Feedback):
    print(f"Received feedback from {feedback.name}: {feedback.message}")
    return {"message": f"Thank you, {feedback.name}! Feedback received."}
