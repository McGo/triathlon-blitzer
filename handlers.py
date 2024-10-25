from detection import Detection


class AHandler:
    def __init__(self):
        pass

    def process(self, detection: Detection):
        pass


class DebuggingHandler(AHandler):
    def process(self, detection: Detection):
        print(detection.time, detection.speed)

