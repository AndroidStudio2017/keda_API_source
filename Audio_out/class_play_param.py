"""

定义输出参数类PlayParam

"""
import os


class PlayParam:
    dictionary = {

    }

    def __init__(self):
        self.audiopath = './audio/audio_out.wav'
        self.cmd = 'aplay'
        self.dictionary = {}

    @property
    def params(self):
        param = ['%s %s' % (key, value) for key, value in self.dictionary.items()]
        result = str(self.cmd)+' '+' '.join(param)+' '+str(self.audiopath)
        return result

    @params.setter
    def params(self, path):
        if isinstance(path, str):
            self.audiopath = path
        else:
            print('Audio Path Type Error: ', path, '----', type(path))

