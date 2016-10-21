from copy import copy
from scan import Scan
import click
import os

current_path = os.getcwd()

@click.command()
@click.option('--base', default=current_path,
                        type=click.Path(exists=True),
                        help='The directory you want to mirror.')
@click.argument('mirror', type=click.Path())
def main(base, mirror):

    base = os.path.expanduser(base)
    mirror = os.path.expanduser(mirror)

    base = os.path.realpath(base)
    mirror = os.path.realpath(mirror)

    # Prevent that mirroring is done to the base folder
    if base == mirror:
        print('Error: The directories can not be the same.')
        return

    if os.path.expanduser(base) in mirror:
        print('Error: Mirror folder can not be a sub-directory of the base folder.')
        return

    # If the mirror folder already exists, ask if the user wants to overwrite it
    if os.path.realpath(mirror):
        i = input('Do you want to overwrite {mirror}? (Y/n) '.format(mirror=mirror))
        if i.lower() not in ["", "y", "yes"]:
            print('Aborting...')
            return

    # Initial mirroring before starting scan
    print(copy(base, mirror))
    s = Scan(base, mirror)
    s.run()

if __name__ == '__main__':
    main()
