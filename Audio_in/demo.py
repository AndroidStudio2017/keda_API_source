"""
用于测试输入音频封装类的demo
"""
import sys
sys.path.append('../../')
import argparse

from src.Audio_in.recordEngine import *

engine = recordEngine()


def _SetTmpWave(tmpWave):
    return engine.SetTmpWave(tmpWave)


def _SetOutWave(outWave):
    return engine.SetOutWave(outWave)


def _SetDuration(duration):
    return engine.SetDuration(duration)


def _SetSampleRate(sampleRate):
    return engine.SetSampleRate(sampleRate)


def _SetChannels(channels):
    return engine.SetChannels(channels)

def _SetFileType(fileType):
    return engine.SetFileType(fileType)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--tmpWave', action='store', dest='tmpWave',
                        help='Set the raw audio path to store')
    parser.add_argument('-o', '--outWave', action='store', dest='outWave',
                        help='Set the final audio(16kHz) path to store')
    parser.add_argument('-d', '--duration', action='store', dest='duration',
                        help='Set the duration of the recording')
    parser.add_argument('-r', '--sampleRate', action='store', dest='sampleRate',
                        help='Set the sample rate of the raw audio')
    parser.add_argument('-c', '--channels', action='store', dest='channels',
                        help='Set the numbers of channels')
    parser.add_argument('-f', '--fileType', action='store', dest='fileType',
                        help='Set the file type of the audio')

    args = parser.parse_args()
    if args.tmpWave:
        if not _SetTmpWave(args.tmpWave):
            print('Argument Error: -t')
            sys.exit(1)

    if args.outWave:
        if not _SetOutWave(args.outWave):
            print('Argument Error: -o')
            sys.exit(1)

    if args.duration:
        if not _SetDuration(args.duration):
            print('Argument Error: -d')
            sys.exit(1)

    if args.sampleRate:
        if not _SetSampleRate(args.sampleRate):
            print('Argument Error: -r')
            sys.exit(1)

    if args.channels:
        if not _SetChannels(args.channels):
            print('Argument Error: -c')
            sys.exit(1)

    if args.fileType:
        if not _SetFileType(args.fileType):
            print('Argument Error: -f')
            sys.exit(1)

    engine.run()
