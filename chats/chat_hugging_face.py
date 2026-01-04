from datetime import datetime

now = datetime.now()
print("Starttime:", now)
print("=========")
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

case = bool(input("Welcome to the game. Press y to continue and enter to discontinue. "))


question = input("Ask anything ")
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    max_new_tokens=200,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto"
)

chat_model = ChatHuggingFace(llm=llm)

result = chat_model.invoke(question)
print(result.content)

case = bool(input("Type y to continue. Press enter to discontinue. "))


print("========")
end_time = datetime.now()
print("End Time", end_time)
print("Total TIme (in seconds): ", (end_time - now).total_seconds())
