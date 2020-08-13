import os
import pickle
pkl_filepath = os.path.expanduser("~/.pywhereisrunning.pkl")


def _getpiddict():
    piddict = None
    if os.path.isfile(pkl_filepath):
        with open(pkl_filepath, 'rb') as f:
            piddict = pickle.load(f)
    return piddict


def _getpid(filename):
    pid = -1
    filename = os.path.abspath(filename)
    piddict = _getpiddict()
    if piddict:
        pid = piddict.get(filename, -1)
    return pid


def _writepid(filename, pid):
    piddict = _getpiddict()
    if piddict is None:
        piddict = {}
    piddict[filename] = pid
    with open(pkl_filepath, 'wb') as f:
        pickle.dump(piddict, f)
