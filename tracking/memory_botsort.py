import numpy as np
from tracking.memory_track import MemoryTrack
from utils.helpers import cosine_similarity
from config import SIMILARITY_THRESHOLD

class MemoryBoTSORT:
    def __init__(self, feature_extractor):
        self.tracks = []
        self.feature_extractor = feature_extractor

    def update(self, frame, detections):
        if len(detections) == 0:
            return np.empty((0, 5))

        bboxes = detections[:, :4]
        features, _ = self.feature_extractor.extract(frame, bboxes)

        results = []

        for i, bbox in enumerate(bboxes):
            matched = False

            for track in self.tracks:
                sim = cosine_similarity(track.feature, features[i])

                if sim > SIMILARITY_THRESHOLD:
                    track.update(bbox, features[i])
                    matched = True
                    results.append([*bbox, track.track_id])
                    break

            if not matched:
                new_track = MemoryTrack(bbox, features[i])
                self.tracks.append(new_track)
                results.append([*bbox, new_track.track_id])

        return np.array(results)