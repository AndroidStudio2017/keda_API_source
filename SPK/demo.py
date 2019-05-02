import sys
sys.path.append('../../')
import argparse

from src.SPK.SPKEngine import *


engine = SPKEngine()


def _GetDataLen():
    return engine.GetDataLen()


def _SetOffSet(offset):
    return engine.SetOffset(offset)


def _SetAudioPath(audioPath):
    return engine.SetAudioPath(audioPath)


def _SetNDesiredNum(nDesiredNum):
    return engine.SetNDesiredNum(nDesiredNum)


def _SetDataLen(dataLen):
    return engine.SetDataLen(dataLen)


def _SetPiceLen(piceLen):
    return engine.SetPiceLen(piceLen)


def _SetWorkType(workType):
    return engine.SetWorkType(workType)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-w', '--worktype', action='store', dest='workType',
                        help='Specify work type (all is default, once can be chosen)')
    parser.add_argument('-p', '--path', action='store', dest='audioPath',
                        help='set audio path which is to be recognized(both)')
    parser.add_argument('-d', '--desired', action='store', dest='nDesiredNum',
                        help='specify the desired num of speakers(both)')
    parser.add_argument('-o', '--offset', action='store', dest='offset',
                        help='specify the beginning of recognition(once)')
    parser.add_argument('-l', '--length', action='store', dest='dataLen',
                        help='specify the length of recognition(once)')
    parser.add_argument('-s', '--step', action='store', dest='piceLen',
                        help='specify pace length for recognition(all)')
    parser.add_argument('-t', '--total', action='store_true', dest='totalLen',
                        help='Get the length of whole audio (must load the audio first)')

    args = parser.parse_args()
    if args.totalLen:
        print('\nTotal frames: ', _GetDataLen().value)
        sys.exit(0)

    if args.workType:
        if not _SetWorkType(args.workType):
            print('Argument Error: -w')
            sys.exit(1)

    if args.audioPath:
        if not _SetAudioPath(args.audioPath):
            print('Argument Error: -p')
            sys.exit(1)

    if args.nDesiredNum:
        if not _SetNDesiredNum(args.nDesiredNum):
            print('Argument Error: -d')
            sys.exit(1)

    if args.offset:
        if not _SetOffSet(args.offset):
            print('Argument Error: -o')
            sys.exit(1)

    if args.dataLen:
        if not _SetDataLen(args.dataLen):
            print('Argument Error: -l')
            sys.exit(1)

    if args.piceLen:
        if not _SetPiceLen(args.piceLen):
            print('Argument Error: -s')
            sys.exit(1)

    engine.run()
