import json

class RAGRetriever:
    def __init__(self, file_path):
        self.records = []

        with open(file_path, "r") as f:
            for line in f:
                self.records.append(json.loads(line))

    def search(self, query):
        query = query.lower()
        results = []

        for r in self.records:
            # Match action
            if r["action"] in query:
                results.append(r)

            # Match person ID
            if f"person {r['person_id']}" in query:
                results.append(r)

        # Remove duplicates
        unique_results = list({(r['frame'], r['person_id']): r for r in results}.values())

        return unique_results[:5] if unique_results else self.records[:5]