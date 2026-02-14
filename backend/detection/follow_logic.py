import math

class FollowDetector:
    def __init__(self,
                 min_frames=25,
                 distance_thresh=160,
                 direction_similarity=0.8):

        self.min_frames = min_frames
        self.distance_thresh = distance_thresh
        self.direction_similarity = direction_similarity

        self.history = {}   # (id1, id2) -> frame_count
        self.prev_positions = {}

    def _direction(self, p1_old, p1_new):
        dx = p1_new[0] - p1_old[0]
        dy = p1_new[1] - p1_old[1]
        mag = math.hypot(dx, dy)
        if mag == 0:
            return (0, 0)
        return (dx / mag, dy / mag)

    def check(self, tracked):
        ids = list(tracked.keys())
        detected = False

        for i in range(len(ids)):
            for j in range(len(ids)):
                if i == j:
                    continue

                id1, id2 = ids[i], ids[j]

                p1 = tracked[id1]
                p2 = tracked[id2]

                dist = math.hypot(p1[0] - p2[0], p1[1] - p2[1])

                if dist > self.distance_thresh:
                    self.history.pop((id1, id2), None)
                    continue

                if id1 not in self.prev_positions or id2 not in self.prev_positions:
                    continue

                d1 = self._direction(self.prev_positions[id1], p1)
                d2 = self._direction(self.prev_positions[id2], p2)

                dot = d1[0]*d2[0] + d1[1]*d2[1]

                if dot > self.direction_similarity:
                    key = (id1, id2)
                    self.history[key] = self.history.get(key, 0) + 1

                    if self.history[key] >= self.min_frames:
                        detected = True
                else:
                    self.history.pop((id1, id2), None)

        self.prev_positions = tracked.copy()
        return detected
