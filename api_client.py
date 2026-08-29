import requests
from dotenv import load_dotenv
import os
import file_utils

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("OPENAI_API_KEY is missing.")

headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
}

def ask_llm(prompt):
    data = {
            "model": "gpt-5.4-mini",
            "input": prompt
    }

    response = requests.post(
            "https://api.openai.com/v1/responses",
            headers=headers,
            json=data
    )

    response.raise_for_status()

    response_data = response.json()
    
    for output in response_data.get("output", []):
        for content in output.get("content", []):
            if content.get("type") == "output_text":
                return content["text"]

    raise ValueError("No text answer found in API response.")
