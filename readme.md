AI Lead Classifier API

An intelligent microservice designed to classify inbound leads using Large Language Models. This API analyzes sales intent and categorizes leads into HOT, WARM, or COLD status.

Stack
Python 3.11, FastAPI, OpenAI SDK, Ollama, Docker.

Project Structure
app/main.py: API endpoints and server setup.
app/ai_service.py: LLM integration logic.
Dockerfile: Container configuration.
.env: Configuration and API keys.

How to Run
1. Install dependencies:
pip install -r requirements.txt

2. Start the local AI (Ollama):
ollama run llama3

3. Run the API:
uvicorn app.main:app --reload

API Usage
Endpoint: POST /analyze-lead
Request Body:
{
  "name": "John Doe",
  "message": "I need a quote for 50 licenses by tomorrow."
}

Response Example:
{
  "score": "HOT",
  "reasoning": "High urgency and clear purchase intent."
}
