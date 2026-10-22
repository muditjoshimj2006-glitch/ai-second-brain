from google import genai
from app.config import API_KEY


client = genai.Client(api_key=API_KEY)

def ai_analysis(text):
    prompt = f"""You are an expert document analyst, read the following {text} and :-
1. Generate a short summary.
2. Use simple English.
3. Avoid technical jargon.
4. Keep the response professional.
5. Maximum 150 words.
    """

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text

