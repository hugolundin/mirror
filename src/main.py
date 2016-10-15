from distutils.dir_util import copy_tree
import os.path
from scan import Scan
import click

current_path = os.path.dirname(os.path.abspath(__file__))

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

    # Mirror folder before starting scan
    print(copy(base, mirror))

    s = Scan(base, mirror)
    s.run()

def copy(base, mirror):
    copy_tree(base, mirror, update=1)
    return ("Copied '{base}' to '{mirror}'".format(base=base, mirror=mirror))


if __name__ == '__main__':
    main()



