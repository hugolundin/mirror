from watchdog.events import LoggingEventHandler
from copy import copy

class Event(LoggingEventHandler):
    def __init__(self, base, mirror):
        self.base = base
        self.mirror = mirror

    def dispatch(self, event):
        print(copy(self.base, self.mirror))