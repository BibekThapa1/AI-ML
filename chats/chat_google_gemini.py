from dotenv import load_dotenv
load_dotenv()

from datetime import datetime

time = datetime.now()
print("Started. Time:", time)

from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-3-pro-preview",
    temperature=1.0,  # Gemini 3.0+ defaults to 1.0
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

result = model.invoke("What is your name?")
print(result.content)

end_time = datetime.now()
print("End time: ", end_time)

print("Total time: (in seconds)", (end_time - time).total_seconds)