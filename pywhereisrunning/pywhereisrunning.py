import os
import signal


def print_linenum(signum, frame):
    import sys
    import inspect
    callerframerecord = inspect.stack()[1]
    # frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    message = ''
    print(os.path.abspath(info.filename), 'func=%s' %
          info.function, 'line=%s:' % info.lineno, message)
    # print("Currently at line", frame.f_code.co_filename, frame.f_lineno)


def _execute():
    # print('kill -SIGUSR1', os.getpid())
    print('pywhereisrunning.py', os.getpid())
    signal.signal(signal.SIGUSR1, print_linenum)


def _main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('pid')
    args = parser.parse_args()
    pid = args.pid
    os.system("bash -c 'kill -SIGUSR1 " + str(pid) + "'")


if __name__ == '__main__':
    _main()
else:
    _execute()
