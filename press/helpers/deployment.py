import os
from press.cli import run


def mount(argument):
    run('mount %s' % argument)
    pass


def mount_root():
    run('mount -T /mnt/press_fstab /mnt/press')


def mkdir(directory):
    run('mkdir -p %s' % directory)
    pass


def mount_disk():
    pass


def recursive_makedir(path, mode=0775):
    if os.path.isdir(path):
        return False

    if os.path.exists(path):
        raise IOError('%s exists but is NOT a directory' % path)

    os.makedirs(path, mode)
    return True