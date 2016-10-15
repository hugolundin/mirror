import os.path
from scan import Scan
from copy import copy
import click

current_path = os.path.dirname(os.path.abspath(__file__))

@click.command()
@click.option('--base', default=current_path,
                        type=click.Path(exists=True),
                        help='The directory you want to mirror.')
@click.argument('mirror', type=click.Path())
def main(base, mirror):

    if base == mirror:
        print('Error: The directories can not be the same.')
        return

    # Initial mirroring before starting scan
    print(copy(base, mirror))
    s = Scan(base, mirror)
    s.run()

if __name__ == '__main__':
    main()



