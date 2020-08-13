import os
import signal
from pywhereisrunning import utils


def print_linenum(signum, _):
    # import inspect
    import sys
    filename = os.path.abspath(sys.argv[0])
    if not filename.endswith("bin/pywhereisrunning"):
        import traceback
        print()
        traceback.print_stack()
    # for callerframerecord in inspect.stack():
    #     # callerframerecord = inspect.stack()[1]
    #     frame = callerframerecord[0]
    #     info = inspect.getframeinfo(frame)
    #     message = ''
    #     print(os.path.abspath(info.filename), 'func=%s' %
    #           info.function, 'line=%s:' % info.lineno, message)


def _execute():
    # print('kill -SIGUSR1', os.getpid())
    import sys
    filename = os.path.abspath(sys.argv[0])
    if not filename.endswith("bin/pywhereisrunning"):
        print('pywhereisrunning', os.getpid())
        signal.signal(signal.SIGUSR1, print_linenum)
        utils._writepid(filename, os.getpid())


if not __name__ == '__main__':
    _execute()
