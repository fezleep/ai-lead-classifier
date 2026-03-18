from fastapi import FastAPI
from app.ai_service import LeadScorer
from pydantic import BaseModel

app = FastAPI(title="Lead Qualification API", version="1.0.0")
scorer = LeadScorer()

class LeadRequest(BaseModel):
    name: str
    message: str

@app.get("/health")
def health_check():
    return {"status": "online"}

@app.post("/analyze-lead")
async def analyze_lead(lead: LeadRequest):
    """
    Endpoint to process and classify incoming leads.
    """
    result = scorer.analyze_lead(lead.name, lead.message)
    return result