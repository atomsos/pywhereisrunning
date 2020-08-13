import os
import pickle
from pywhereisrunning import utils


def _main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    filename = args.filename
    if filename.isdigit():
        pid = filename
    else:
        pid = utils._getpid(filename)
    if pid == -1:
        raise Exception(filename + ' pid not found')
    os.system("bash -c 'kill -SIGUSR1 " + str(pid) + "'")


if __name__ == '__main__':
    _main()
