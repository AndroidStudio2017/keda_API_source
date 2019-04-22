import sys
sys.path.append('../../')

import argparse
from src.ISR.ISREngine import *

engine = ISREngine()


def _SetRecognitionEngine(e):
    return engine.setEngine(e)


def _SetAudioPath(audioPath):
    return engine.setAudioPath(audioPath)


def _SetSDKLanguage(language):
    return engine.setSDKLanguage(language)


def _SetSDKAccent(accent):
    return engine.setSDKAccent(accent)


def _SetSDKSampleRate(sampleRate):
    return engine.setSDKSampleRate(sampleRate)


def _SetWebEngineType(engineType):
    return engine.setWebEngineType(engineType)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-w', '--web', action='store_true', dest='webChoose', default=False, help='use web api to recognize (default SDK)(all)')
    parser.add_argument('-p', '--path', action='store', dest='audioPath', help='set audio path which is to be recognized(all)')
    parser.add_argument('-l', '--language', action='store', dest='language', help='set audio language(just in sdk)')
    parser.add_argument('-a', '--accent', action='store', dest='accent', help='set special accent(just in sdk)')
    parser.add_argument('-r', '--sampleRate', action='store', dest='sampleRate', help='set audio sample rate(just in sdk)')
    parser.add_argument('-e', '--engineType', action='store', dest='engineType', help='set recognizing engine type (sms16k,sms8k,sms-en8)(just in web)')

    args = parser.parse_args()
    if args.webChoose:
        if not _SetRecognitionEngine('web'):
            print('Argument Error: -w')
            sys.exit(1)
    else:
        if not _SetRecognitionEngine('sdk'):
            print('Argument Error: -w')
            sys.exit(1)

    if args.audioPath is not None:
        if not _SetAudioPath(args.audioPath):
            print('Argument Error: -p')
            sys.exit(1)

    if args.language is not None:
        if not _SetSDKLanguage(args.language):
            print('Argument Error: -l')
            sys.exit(1)

    if args.accent is not None:
        if not _SetSDKAccent(args.accent):
            print('Argument Error: -a')
            sys.exit(1)

    if args.sampleRate is not None:
        if not _SetSDKSampleRate(args.sampleRate):
            print('Argument Error: -r')
            sys.exit(1)

    if args.engineType is not None:
        if not _SetWebEngineType(args.engineType):
            print('Argument Error: -e')
            sys.exit(1)

    res = engine.run()
    print(res)
    sys.exit(0)

