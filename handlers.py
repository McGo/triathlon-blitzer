from detection import Detection
from abc import ABC


class AHandler(ABC):
    def __init__(self):
        pass

    def process(self, detection: Detection):
        pass


class ConfigurableActionsHandler(AHandler):

    def __init__(self, actions):
        super().__init__()
        self.actions = actions

    def process(self, detection: Detection):
        for action in self.actions:
            action.perform(detection)
