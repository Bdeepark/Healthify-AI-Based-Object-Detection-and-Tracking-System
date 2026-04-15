from rag.json_storage import JSONStorage
from rag.action_mapping import ActionMapper

class MetadataGenerator:
    def __init__(self):
        self.storage = JSONStorage()
        self.action_mapper = ActionMapper()  # ✅ NEW

    def add(self, frame, track_id, bbox):
        # Get action from mapper
        action = self.action_mapper.map_action(track_id, bbox)

        record = {
            "frame": int(frame),
            "person_id": int(track_id),
            "bbox": list(map(int, bbox)),
            "action": action
        }

        self.storage.add(record)

    def save(self, path):
        self.storage.save(path)