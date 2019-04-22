"""

定义了TTSParams类, 封装了Web语音合成参数

"""
from collections import OrderedDict


class TTSParams:
    """
    Web语音合成参数类
    """

    def __init__(self):
        """
        初始化默认参数
        """
        self._TTSParams = OrderedDict()
        self._TTSParams['auf'] = 'audio/L16;rate=16000'
        self._TTSParams['aue'] = 'raw'
        self._TTSParams['voice_name'] = 'xiaoyan'
        self._TTSParams['speed'] = '50'
        self._TTSParams['volume'] = '50'
        self._TTSParams['pitch'] = '50'
        self._TTSParams['engine_type'] = 'intp65'
        self._TTSParams['text'] = 'text'

    def SetAuf(self,auf):
        _state = True
        if isinstance(auf, str):
            self._TTSParams['auf'] = auf
        else:
            print('AUF in TTS has a wrong type: ', type(auf))
            _state = False
        return _state

    def SetAue(self, aue):
        _state = True
        if isinstance(aue, str):
            self._TTSParams['aue'] = aue
        else:
            print('AUE in TTS has a wrong type: ', type(aue))
            _state = False
        return _state

    def SetEngineType(self, engineType):
        _state = True
        if isinstance(engineType, str):
            self._TTSParams['engine_type'] = engineType
        else:
            print('Engine Type in TTS has a wrong type: ', type(engineType))
            _state = False
        return _state

    def SetText(self, text):
        _state = True
        if isinstance(text, str):
            self._TTSParams['text'] = text
        else:
            print('text in TTS has a wrong type: ', type(text))
            _state = False
        return _state

    def SetVoiceByName(self, voiceName):
        """
        设置合成声音, 具体需要查看文档
        :param voiceName: 声音名字
        :return: None
        """
        if isinstance(voiceName, str):
            self._TTSParams['voice_name'] = voiceName
            return True
        else:
            print("Voice Name in TTS has a wrong type: ", type(voiceName))
            return False

    def SetSpeed(self, speed):
        """
        设置合成声音语速
        :param speed: int 语速 0~100 or str
        :return: Success or fail
        """
        if isinstance(speed, str):
            self._TTSParams['speed'] = speed
            return True
        elif isinstance(speed, int):
            self._TTSParams['speed'] = str(speed)
            return True
        else:
            print("Speech Speed int TTS has a wrong type: ", type(speed))
            return False

    def SetVolume(self, volume):
        """
        设置合成声音大小
        :param volume: int 声音大小 0~100 or str
        :return: Success or fail
        """
        if isinstance(volume, str):
            self._TTSParams['volume'] = volume
            return True
        elif isinstance(volume, int):
            self._TTSParams['volume'] = str(volume)
            return True
        else:
            print("Speech Volume int TTS has a wrong type: ", type(volume))
            return False

    def SetPitch(self, pitch):
        """
        设置合成声音语调
        :param pitch: int 声音语调 0~100 or str
        :return: Success or fail
        """
        if isinstance(pitch, str):
            self._TTSParams['pitch'] = pitch
            return True
        elif isinstance(pitch, int):
            self._TTSParams['pitch'] = str(pitch)
            return True
        else:
            print("Speech Pitch int TTS has a wrong type: ", type(pitch))
            return False

    @property
    def Params(self):
        res = ["%s:%s" % ('\"'+key+'\"', '\"'+value+'\"') for key, value in self._TTSParams.items()]
        res = ','.join(res)
        res = '{' + res + '}'
        print(res)
        return res

    @Params.setter
    def Params(self, value):
        if isinstance(value, str):
            values = value.split(',')
            for kv in values:
                kvs = kv.split(':', 2)
                if len(kvs) == 2:
                    self._TTSParams[kvs[0].strip()] = kvs[1].strip()
        elif isinstance(value, dict):
            self._TTSParams.update(value)


if __name__ == '__main__':
    param = TTSParams()
    print(param.Params)

    testP = "aue:raw,auf:audio/L16;rate=8000,voice_name:xiaoyan,engine_type:intp65"
    param.Params = testP
    print(param.Params)
