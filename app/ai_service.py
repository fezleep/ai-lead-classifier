import os
from openai import OpenAI

class LeadScorer:
    def __init__(self):
        
        self.client = OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama"
        )

    def analyze_lead(self, lead_name: str, message: str):
    
        prompt = f"""
        Objective: Classify the following sales lead.
        Lead: {lead_name}
        Message: "{message}"

        Rules:
        - HOT: Intent to buy, pricing request, or demo request.
        - WARM: Interest shown, but asking general questions.
        - COLD: No intent, "just looking", or vague.

        Constraint: Return ONLY a valid JSON object. No intro, no outro.
        Format: {{"score": "HOT|WARM|COLD", "reasoning": "brief explanation"}}
        """

        response = self.client.chat.completions.create(
            model="llama3",
            messages=[{"role": "user", "content": prompt}],
            temperature=0  
        )
        
        return response.choices[0].message.content