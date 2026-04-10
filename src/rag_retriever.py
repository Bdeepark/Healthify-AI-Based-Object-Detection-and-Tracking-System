import json
from sentence_transformers import SentenceTransformer, util


class RAGRetriever:
    def __init__(self, file_path):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.records = []
        self.texts = []

        with open(file_path, "r") as f:
            for line in f:
                item = json.loads(line)

                for p in item["persons"]:
                    record = {
                        "timestamp": item["timestamp"],
                        "role": p["role"].lower(),
                        "action": p["action_name"].lower()
                    }

                    self.records.append(record)

                    text = f"{record['timestamp']} | {record['role']} performing {record['action']}"
                    self.texts.append(text)

        self.embeddings = self.model.encode(self.texts, convert_to_tensor=True)

    def retrieve(self, query, top_k=5):
        query_emb = self.model.encode(query, convert_to_tensor=True)
        scores = util.cos_sim(query_emb, self.embeddings)[0]
        top_results = scores.topk(k=top_k)

        return [self.records[i] for i in top_results.indices]