from distutils.dir_util import copy_tree
from os.path import dirname, abspath
from watchdog.events import LoggingEventHandler
from watchdog.observers import Observer
import click
import time

# TODO: Prevent mirror == base directory.

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

class Event(LoggingEventHandler):

    def __init__(self, base, mirror):
        self.base = base
        self.mirror = mirror

    def dispatch(self, event):
        print(copy(self.base, self.mirror))

current_path = dirname(abspath(__file__))

@click.command()
@click.option('--base', default=current_path,
                        type=click.Path(exists=True),
                        help='The directory you want to mirror.')
@click.argument('mirror', type=click.Path())
def main(base, mirror):

    # Prevent usage of the same directory
    if base == mirror:
        print('Error: The directories can not be the same.')
        return

    s = Scan(base, mirror)
    s.run()

def copy(base, mirror):
    copy_tree(base, mirror, update=1)
    return ("Copied '{base}' to '{mirror}'".format(base=base, mirror=mirror))


if __name__ == '__main__':
    main()



