import numpy as np

class ActionMapper:
    def __init__(self):
        # Store previous positions of each track
        self.prev_positions = {}

    def map_action(self, track_id, bbox):
        """
        Simple motion-based action detection
        """
        x1, y1, x2, y2 = bbox
        cx = (x1 + x2) / 2
        cy = (y1 + y2) / 2

        action = "standing"

        if track_id in self.prev_positions:
            px, py = self.prev_positions[track_id]

            dx = abs(cx - px)
            dy = abs(cy - py)

            # Motion threshold
            if dx > 10 or dy > 10:
                action = "walking"
            else:
                action = "standing"

        # Update position
        self.prev_positions[track_id] = (cx, cy)

        return action