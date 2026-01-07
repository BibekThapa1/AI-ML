from datetime import datetime

now = datetime.now()
print("Starttime:", now)
print("=========")
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

case = bool(input("Welcome to the game. Press y to continue and enter to discontinue. "))

template = ChatPromptTemplate(
    [
        ("system", "You are a helpful AI bot. Your name is {name}."),
        ("human", "Hello, how are you doing?"),
        ("ai", "I'm doing well, thanks!"),
        ("human", "{user_input}"),
    ]
)
llm = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-R1-0528",
        task="text-generation",
        max_new_tokens=200,
        do_sample=False,
        repetition_penalty=1.03,
        provider="auto"
    )


chat_model = ChatHuggingFace(llm=llm)

while case:
    question = input("Ask anything ")
    result = chat_model.invoke(question)
    print(result.content)

    case = bool(input("Type y to continue. Press enter to discontinue. "))


print("========")
end_time = datetime.now()
print("End Time", end_time)
print("Total TIme (in seconds): ", (end_time - now).total_seconds())
