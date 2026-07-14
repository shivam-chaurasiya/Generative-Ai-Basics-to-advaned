from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Piyush Garg.
    You are acting on behalf of Piyush Garg who is 25 years old Tech enthusiatic and 
    principle engineer. Your main tech stack is JS and Python and You are leaning GenAI these days.

    Examples:
    Q. Hey
    A: Hey, Whats up!

    (100 - 150 examples)
"""

response = client.chat.completions.create(
    model = "gemini-3.5-flash", 
     messages=[
        { "role": "system", "content": SYSTEM_PROMPT},
        { "role": "user", "content": "Who are you ?"}
    ]
)

print(response.choices[0].message.content)