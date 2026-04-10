import json

class JSONStorage:
    def __init__(self, path="data/metadata.jsonl"):
        self.path = path

    def save(self, metadata):
        with open(self.path, "a") as f:
            f.write(json.dumps(metadata) + "\n")

    def load(self):
        data = []
        with open(self.path, "r") as f:
            for line in f:
                data.append(json.loads(line))
        return data