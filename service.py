from time import sleep

from detectors import RandomDetector
from handlers import ConfigurableActionsHandler
from actions import TakePictureAction, PrintDetectionAction


def main():
    # setup detector and handler
    detector = RandomDetector()
    handler = ConfigurableActionsHandler([
        TakePictureAction('~/Desktop/images'),
        PrintDetectionAction()
    ])

    while True:
        # Let the detector do its thing to check for a new detection
        detector.detect()

        # If there is one, handle it correctly
        if detector.has_new_detection():
            detection = detector.current_detection
            handler.process(detection)

        # only check every 500ms
        sleep(0.5)


if __name__ == '__main__':
    main()
