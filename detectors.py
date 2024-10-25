import random
from detection import Detection


class ADetector:
    current_detection: Detection = None
    last_detection: Detection = None

    def detect(self):
        pass

    def has_new_detection(self):
        if self.current_detection is None:
            return False
        if self.last_detection is None:
            return True
        if self.current_detection.time > self.last_detection.time:
            return True
        return False


class RandomDetector(ADetector):
    threshold: float

    def __init__(self, threshold=0.5):
        self.threshold = threshold

    def detect(self):
        self.last_detection = self.current_detection
        if random.random() > self.threshold:
            self.current_detection = Detection(speed=random.randint(15, 40))
