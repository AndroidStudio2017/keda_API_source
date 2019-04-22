import sys
sys.path.append('../../')

import argparse
import json

from src.TTS.TTSEngine import *

engine = TTSEngine()


def _SetAudioPath(audioPath):
    return engine.SetAudioPath(audioPath)


def _SetEngine(e):
    return engine.SetEngine(e)


def _SetSrcText(src_text):
    return engine.SetSrcText(src_text)


def _SetSpeed(speed):
    return engine.SetSpeed(speed)


def _SetVolume(volume):
    return engine.SetVolume(volume)


def _SetPitch(pitch):
    return engine.SetPitch(pitch)


def _SetVoiceName(voiceName):
    with open('./voiceName.json', 'r') as fp:
        nameDict = json.load(fp)

    print(nameDict)
    if voiceName not in nameDict.keys():
        return False
    for k, v in nameDict.items():
        if k == voiceName:
            voiceName = v
            break
    return engine.SetVoiceName(voiceName)


def _SetSDKSampleRate(sampleRate):
    return engine.SetSDKSampleRate(sampleRate)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-w', '--web', action='store_true', dest='webChoose', default=False,
                        help='use web api to recognize (default SDK)(all)')
    parser.add_argument('-p', '--path', action='store', dest='audioPath',
                        help='identify the path to store audio result')
    parser.add_argument('-t', '--text', action='store', dest='src_text',
                        help='the source text which is to be TTS')
    parser.add_argument('-s', '--speed', action='store', dest='speed',
                        help='identify the speed of audio result')
    parser.add_argument('-v', '--volume', action='store', dest='volume',
                        help='identify the volume of audio result')
    parser.add_argument('-i', '-pitch', action='store', dest='pitch',
                        help='identity the pitch of audio result')
    parser.add_argument('-n', '--name', action='store', dest='name',
                        help='identify the voice name of audio result')
    parser.add_argument('-r', '--sampleRate', action='store', dest='sampleRate',
                        help='identify the sample rate of audio result')

    args = parser.parse_args()
    if args.webChoose:
        if not _SetEngine('web'):
            print('Argument Error: -w')
            sys.exit(1)
    else:
        if not _SetEngine('sdk'):
            print('Argument Error: -w')
            sys.exit(1)

    if args.audioPath:
        if not _SetAudioPath(args.audioPath):
            print('Argument Error: -p')
            sys.exit(1)

    if args.src_text:
        if not _SetSrcText(args.src_text):
            print('Argument Error: -t')
            sys.exit(1)

    if args.speed:
        if not _SetSpeed(args.speed):
            print('Argument Error: -s')
            sys.exit(1)

    if args.volume:
        if not _SetVolume(args.volume):
            print('Argument Error: -v')
            sys.exit(1)

    if args.pitch:
        if not _SetPitch(args.pitch):
            print('Argument Error: -i')
            sys.exit(1)

    if args.name:
        if not _SetVoiceName(args.name):
            print('Argument Error: -n')
            sys.exit(1)

    if args.sampleRate:
        if not _SetSDKSampleRate(args.sampleRate):
            print('Argument Error: -r')
            sys.exit(1)

    engine.run()
