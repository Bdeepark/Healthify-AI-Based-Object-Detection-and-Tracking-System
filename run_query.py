from src.rag_llm import RAGLLM
from src.rag_retriever import RAGRetriever

retriever = RAGRetriever("data/metadata.jsonl")
llm = RAGLLM()

while True:
    query = input("\nEnter your query: ")

    if query.lower() in ["exit", "quit"]:
        break

    records = retriever.retrieve(query) 

    answer = llm.generate(query, records)  

    print("\n Answer:\n", answer)