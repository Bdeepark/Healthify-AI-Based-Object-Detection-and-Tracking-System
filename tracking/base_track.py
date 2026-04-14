class Track:
    _count = 0

    def __init__(self, bbox, feature):
        self.track_id = Track._count
        Track._count += 1

        self.bbox = bbox
        self.feature = feature
        self.hits = 1
        self.time_since_update = 0
        self.state = "tentative"

    def update(self, bbox, feature):
        self.bbox = bbox
        self.feature = feature
        self.hits += 1
        self.time_since_update = 0

        if self.hits >= 3:
            self.state = "confirmed"