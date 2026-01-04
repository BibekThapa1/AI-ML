from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import HuggingFacePipeline

print("=============")
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(model_id)
print("=============")

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
    temperature=0.7,
)
print("=============")

llm = HuggingFacePipeline(pipeline=pipe)
print("=============")

result = llm.invoke("Explain LangChain in simple words")
print("=============")

print(result)