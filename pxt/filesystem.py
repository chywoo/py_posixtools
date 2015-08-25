__author__ = 'Sungho Park'

import os

__directory_queue = []


def pushd():
    """
    push current directory to queue
    """
    cwd = os.getcwd()

    __directory_queue.append(cwd)


def popd():
    """
    change directory to popped.
    """
    os.chdir(__directory_queue.pop())

