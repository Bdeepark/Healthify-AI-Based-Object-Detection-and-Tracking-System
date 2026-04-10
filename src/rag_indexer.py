import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class RAGIndexer:
    def __init__(self):
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

    def load_json(self, path):
        data = []
        with open(path, "r") as f:
            for line in f:
                data.append(json.loads(line))
        return data

    def convert_to_text(self, metadata):
        texts = []

        for frame in metadata:
            for person in frame["persons"]:
                text = (
                    f"Frame {frame['frame_id']} at {frame['timestamp']}: "
                    f"{person['role']} performing {person['action_name']} "
                    f"(Action ID {person['action_id']})"
                )
                texts.append(text)

        return texts

    def build(self, texts):
        embeddings = self.embedder.encode(texts)
        dim = embeddings.shape[1]

        index = faiss.IndexFlatL2(dim)
        index.add(np.array(embeddings))

        return index, texts