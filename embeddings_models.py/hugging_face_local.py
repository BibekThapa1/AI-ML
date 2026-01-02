from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-miniLM-L6-v2'
)

text = "Kathmandu is the capital city of Nepal."

vector = embedding.embed_query(text)

print(vector)