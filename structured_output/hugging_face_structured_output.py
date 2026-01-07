from dotenv import load_dotenv
load_dotenv()
from typing import TypedDict


class ApplicationLetter(TypedDict):
    subject: float
    body: str

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

llm = HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-R1-0528',
    task="text-generation",
    provider="auto"
)

model = ChatHuggingFace(llm=llm)
structured_model = model.with_structured_output(ApplicationLetter)

result = structured_model.invoke("Write an application for sick leave to a school. The reason is due to headache,")
print(result)