FastAPI NLP Sentiment Analyzer with Authentication and Rate Limiting

📌 Description
This project is a web API built using FastAPI that integrates with the Google Cloud Natural Language API to perform:

Sentiment Analysis
Entity Recognition
Syntax Analysis

It also implements API Key Authentication and Rate Limiting to ensure secure and controlled access.

📌 Features
Sentiment Analysis (positive, negative, neutral)
Entity Recognition (people, places, organizations)
Syntax Analysis (grammar, parts of speech)
API Key Authentication
Rate Limiting (prevents abuse)
Input validation and error handling
Environment-based configuration

📌 Prerequisites
Python 3.10+
Google Cloud account
Enabled Natural Language API
API Key

📌 Installation
git clone <https://github.com/ThiafFaith/fastapi-nlp-project.git>
cd fastapi-nlp
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn requests python-dotenv slowapi

📌 Configuration
GOOGLE_API_KEY=your_google_api_key
API_SECRET_KEY=your_secret_key_here

📌 API Endpoints
POST /analyze
Request:
{
  "text": "I love FastAPI"
}
Headers:
x-api-key: mysecurekey123
Response:
{
  "documentSentiment": {
    "score": 0.9,
    "magnitude": 0.9
  }
}

📌 Authentication

This API uses API Key Authentication.

The client must include:
x-api-key: your_secret_key_here

If invalid or missing:
401 Unauthorized

📌 Rate Limiting

Implemented using SlowAPI:

/analyze, /entities, /syntax → 3 requests/minute
/analyze-all → 2 requests/minute

If exceeded:

429 Too Many Requests

📌 Testing Instructions

Run server:

uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000/docs
Use Swagger UI to test endpoint.

📌 Troubleshooting
Issue					Solution
401 Unauthorized		Check API key
429 Error				Wait for rate limit reset
500 Error				Check Google API key
Infinite loading		Check internet / API response

📌 Cost Control (Free Tier Safety)

This project is configured to stay within free-tier limits:

📌 Rate limiting (3/minute)
Input size restriction (max 200 chars)
API key restrictions in Google Cloud

📥 How to Clone & Run

Add this section:

git clone https://github.com/ThiafFaith/fastapi-nlp-project.git

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

⚙️ Setup Environment Variables

Create .env file:

GOOGLE_API_KEY=your_api_key
API_SECRET_KEY=mysecurekey123

📌 Team Members
Faith – Coding 
Meliza Belingen & Brad Lee Fesway– Powerpoint
Beverly Bakisan, Juvinal Sikwan, Jimini Tangpep- Demonstration
