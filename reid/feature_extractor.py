import numpy as np

class FeatureExtractor:
    def extract(self, frame, bboxes):
        features = []
        qualities = []

        for _ in bboxes:
            f = np.random.rand(128)
            f = f / np.linalg.norm(f)
            features.append(f)
            qualities.append(1.0)

        return np.array(features), qualities