from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model='gpt-5-nano')

result = llm.invoke("What is your name")
print(result.content)