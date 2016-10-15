from distutils.dir_util import copy_tree

def copy(base, mirror):
    copy_tree(base, mirror, update=1)
    return ("Mirroring '{base}' to '{mirror}'.".format(base=base,
                                                       mirror=mirror))