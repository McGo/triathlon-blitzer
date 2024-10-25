import time
from abc import ABC

from detection import Detection


class AAction(ABC):

    def perform(self, detection: Detection):
        pass


class TakePictureAction(AAction):
    def __init__(self, path: str):
        self.path = path

    def perform(self, detection: Detection):
        try:
            filename_prefix = time.strftime("%Y-%m-%d-%H%M%S", time.gmtime(detection.time))
            print(filename_prefix)
            from picamzero import Camera
            cam = Camera()
            cam.start_preview()
            cam.take_photo(self.path + "/" +filename_prefix + ".jpg")
            cam.stop_preview()
        except Exception as e:
            print('Trying to take picture but got error ' + str(e))


class PrintDetectionAction(AAction):

    def perform(self, detection: Detection):
        print(detection.time, detection.speed)
