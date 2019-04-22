"""

定义了 TTSSessionParam类, 封装了语音合成会话参数

"""
from collections import OrderedDict


class TTSSessionParam:
    """
    语音合成参数类
    """
    def __init__(self):
        """
        初始化默认参数
        """
        self._session_begin_params = OrderedDict()
        self._session_begin_params['voice_name'] = 'xiaoyan'
        self._session_begin_params['text_encoding'] = 'utf8'
        self._session_begin_params['sample_rate'] = '16000'
        self._session_begin_params['speed'] = '50'
        self._session_begin_params['volume'] = '50'
        self._session_begin_params['pitch'] = '50'
        self._session_begin_params['rdn'] = '2'

    def SetSampleRate(self, sampleRate):
        """
        设置合成声音采样率，具体需查看文档
        :param sampleRate: 采样率
        :return: Success or Fail
        """
        if isinstance(sampleRate, str):
            self._session_begin_params['sample_rate'] = sampleRate
            return True
        elif isinstance(sampleRate, int):
            self._session_begin_params['sample_rate'] = str(sampleRate)
            return True
        else:
            print('Sample Rate in TTS has a wrong type: ', type(sampleRate))
            return False

    def SetVoiceByName(self, voiceName):
        """
        设置合成声音, 具体需要查看文档
        :param voiceName: 声音名字
        :return: Success or Fail
        """
        if isinstance(voiceName, str):
            self._session_begin_params['voice_name'] = voiceName
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
            self._session_begin_params['speed'] = speed
            return True
        elif isinstance(speed, int):
            self._session_begin_params['speed'] = str(speed)
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
            self._session_begin_params['volume'] = volume
            return True
        elif isinstance(volume, int):
            self._session_begin_params['volume'] = str(volume)
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
            self._session_begin_params['pitch'] = pitch
            return True
        elif isinstance(pitch, int):
            self._session_begin_params['pitch'] = str(pitch)
            return True
        else:
            print("Speech Pitch int TTS has a wrong type: ", type(pitch))
            return False

    @property
    def params(self):
        """
        合成传给讯飞的参数
        :return: 用,分割参数的字符串
        """
        results = ['%s = %s' % (key, value) for key, value in self._session_begin_params.items()]
        return ','.join(results)

    @params.setter
    def params(self, value):
        """
        设置参数值
        :param value: 设置参数值(接受字符串和字典)
        :return:
        """
        if isinstance(value, str):
            values = value.split(',')
            for kv in value:
                kvs = kv.split('=', 2)
                if len(kvs) == 2:
                    self._session_begin_params[kvs[0].strip()] = kvs[1].strip()
        elif isinstance(value, dict):
            self._session_begin_params.update(value)
