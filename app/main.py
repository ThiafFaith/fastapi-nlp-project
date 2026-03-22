from fastapi import FastAPI, Depends, HTTPException, Request
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv
from app.auth import verify_api_key
from app.limiter import limiter

load_dotenv()

app = FastAPI()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

class TextRequest(BaseModel):
    text: str

@app.post("/analyze")
@limiter.limit("3/minute")
async def analyze(request: Request, data: TextRequest, api_key: str = Depends(verify_api_key)):

    if len(data.text) > 200:
        raise HTTPException(status_code=400, detail="Text too long")

    url = f"https://language.googleapis.com/v1/documents:analyzeSentiment?key={GOOGLE_API_KEY}"

    body = {
        "document": {
            "type": "PLAIN_TEXT",
            "content": data.text
        }
    }

    try:
        res = requests.post(url, json=body, timeout=5)
        return res.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))