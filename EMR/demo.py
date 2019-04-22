import sys
sys.path.append('../../')

import argparse

from src.EMR.EMREngine import *

engine = EMREngine()


def _SetAudioPath(audioPath):
    return engine.SetAudioPath(audioPath)


def _SetResource(resource):
    return engine.SetResouce(resource)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--path', action='store', dest='path',
                        help='set audio path which is to be recognized')
    parser.add_argument('-r', '--resource', action='store', dest='resource',
                        help='set the directory of resource files')

    args = parser.parse_args()
    if args.path:
        if not _SetAudioPath(args.path):
            print('Argument Error: -p')
            sys.exit(1)

    if args.resource:
        if not _SetResource(args.resource):
            print('Argument Error: -p')
            sys.exit(1)

    engine.run()
