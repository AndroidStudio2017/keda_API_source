"""
用于测试输出音频封装类的demo
"""
import sys
sys.path.append('../../')

import argparse

from src.Audio_out.playEngine import *

engine = playEngine()


def _SetAudioPath(audioPath):
    return engine.SetAudioPath(audioPath)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--path', action='store', dest='path',
                        help='Set the audio path to play')

    args = parser.parse_args()
    if args.path:
        if not _SetAudioPath(args.path):
            print('Argument Error: -p')
            sys.exit(1)

    engine.run()
