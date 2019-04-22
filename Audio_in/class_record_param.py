"""

定义输入参数类RecordParam

"""


class RecordParam:
    dictionary = {

    }

    def __init__(self):
        """
        初始化默认参数
        """
        # self.dictionary['-D'] = 'hw1,0'
        self.dictionary['-d'] = '10'
        self.dictionary['-f'] = 'cd'
        self.dictionary['-r'] = '16000'
        self.dictionary['-c'] = '1'
        self.dictionary['-t'] = 'wav'
        self.cmd = 'arecord'
        self.audioPath = './audio/test.wav'

    def GetAudioPath(self):
        return str(self.audioPath)

    def SetAudioPath(self, audioPath):
        _state = True
        if isinstance(audioPath, str):
            self.audioPath = audioPath
        else:
            _state = False
        return _state

    @property
    def params(self):
        """
        将字典形式dict转化为直接可以执行的shell命令
        :return: shell命令
        """
        param = ['%s %s' % (key, value) for key,value in self.dictionary.items()]
        result = str(self.cmd)+' '+' '.join(param)+' '+str(self.audioPath)
        return result

    @params.setter
    def params(self, value):
        if isinstance(value, dict):
            self.dictionary.update(value)
        else:
            print('Argument Type Error in record: ', type(value))


