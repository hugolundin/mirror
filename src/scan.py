from watchdog.observers import Observer
from event import Event
import time

class Scan:
    def __init__(self, base, mirror):
        self.observer = Observer()
        self.base = base
        self.mirror = mirror

    def run(self):
        event_handler = Event(self.base, self.mirror)
        self.observer.schedule(event_handler, self.base, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(3)
        except KeyboardInterrupt:
            print("Stopping...")
            self.observer.stop()

        self.observer.join()