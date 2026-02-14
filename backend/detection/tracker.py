import math

class PersonTracker:
    def __init__(self, max_distance=80):
        self.next_id = 0
        self.tracks = {}
        self.max_distance = max_distance

    def update(self, centers):
        new_tracks = {}

        for cx, cy in centers:
            matched_id = None
            min_dist = self.max_distance

            for tid, (tx, ty) in self.tracks.items():
                dist = math.hypot(cx - tx, cy - ty)
                if dist < min_dist:
                    matched_id = tid
                    min_dist = dist

            if matched_id is None:
                matched_id = self.next_id
                self.next_id += 1

            new_tracks[matched_id] = (cx, cy)

        self.tracks = new_tracks
        return new_tracks
