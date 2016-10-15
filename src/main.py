from copy import copy
from scan import Scan
import click
import os.path

current_path = os.path.dirname(os.path.abspath(__file__))

@click.command()
@click.option('--base', default=current_path,
                        type=click.Path(exists=True),
                        help='The directory you want to mirror.')
@click.argument('mirror', type=click.Path())
def main(base, mirror):

    # Prevent that mirroring is done to the base folder
    if os.path.realpath(base) == os.path.realpath(mirror):
        print('Error: The directories can not be the same.')
        return

    if os.path.realpath(base) in os.path.realpath(mirror):
        print('Error: Mirror folder can not be a sub-directory of base folder.')
        return

    # If the mirror folder already exists, ask if the user wants to overwrite it
    if os.path.exists(os.path.realpath(mirror)):
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
