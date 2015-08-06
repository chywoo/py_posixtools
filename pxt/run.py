__author__ = 'chywoo'

import argparse

def run(script):
    buffer = None

    commands = script.split("|")

    for cmd in commands:
        buffer = _execute(cmd, buffer)

    return buffer

def _execute(cmd, stdin):
    tokens = cmd.split(" ")

    exec = tokens[0]
    args = tokens[1:]

    parser = argparse.ArgumentParser()
