import datetime
from src.action_mapping import ACTION_MAP

class MetadataGenerator:
    def __init__(self):
        self.frame_id = 0

    def generate(self, tracks, actions):
        metadata = {
            "frame_id": self.frame_id,
            "timestamp": datetime.datetime.now().isoformat(),
            "persons": []
        }

        for track in tracks:
            tid = track["id"]
            action_id = actions.get(tid, "UNKNOWN")

            action_info = ACTION_MAP.get(action_id, {
                "name": "unknown",
                "category": "unknown"
            })

            role = (
                "Patient" if action_info["category"] == "Patient"
                else "Caregiver" if action_info["category"] == "Caregiver"
                else "Unknown"
            )

            metadata["persons"].append({
                "id": tid,
                "action_id": action_id,
                "action_name": action_info["name"],
                "category": action_info["category"],
                "role": role
            })

        self.frame_id += 1
        return metadata