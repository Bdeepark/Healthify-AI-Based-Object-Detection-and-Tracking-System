from src.rag_indexer import RAGIndexer

indexer = RAGIndexer()

metadata = indexer.load_json("data/metadata.jsonl")
texts = indexer.convert_to_text(metadata)

index, texts = indexer.build(texts)

import pickle
with open("data/index.pkl", "wb") as f:
    pickle.dump((index, texts), f)

print("Index built successfully!")