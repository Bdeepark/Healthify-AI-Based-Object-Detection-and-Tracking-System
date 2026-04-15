from tracking.base_track import Track

class MemoryTrack(Track):
    def __init__(self, bbox, feature):
        super().__init__(bbox, feature)
        self.confidence = 1.0

    def predict(self):
        self.time_since_update += 1
        self.confidence *= 0.95

    def mark_missed(self):
        if self.confidence < 0.2:
            self.state = "deleted"