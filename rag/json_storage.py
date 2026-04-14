import json

class JSONStorage:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def save(self, path):
        with open(path, "w") as f:
            for r in self.records:
                f.write(json.dumps(r) + "\n")