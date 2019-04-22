from src.ISR.ISR_API import *


class ISREngine:
    """
    ISREngine类，用于实现ISR
    """
    def __init__(self):
        self._is_error = False
        self._is_running = False
        self._is_web = False
        self.audio_path = './audio/test.wav'

        self.web_engine_type = 'sms16k'
        self.web_aue = 'raw'
        self.sdk_sub = 'iat'
        self.sdk_domain = 'iat'
        self.sdk_language = 'zh_cn'
        self.sdk_accent = 'mandarin'
        self.sdk_sample_rate = '16000'
        self.sdk_result_type = 'plain'
        self.sdk_result_encoding = 'utf8'
        self.sdk_pice_len = 1000

    def setAudioPath(self, audioPath):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(audioPath, str):
            self.audio_path = audioPath
        else:
            self._is_error = True
            _state = False
        return _state

    def setEngine(self, engine):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(engine, str):
            if engine == 'web':
                self._is_web = True
            elif engine == 'sdk':
                self._is_web = False
            else:
                self._is_error = True
                _state = False
        else:
            self._is_error = True
            _state = False
        return _state

    def setWebEngineType(self, engineType):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(engineType, str):
            if engineType in WEB_ENGINE_TYPE:
                self.web_engine_type = engineType
            else:
                self._is_error = True
                _state = False
        else:
            self._is_error = True
            _state = False
        return _state

    def setWebAue(self, aue):
        pass

    def setSDKSub(self, sub):
        pass

    def setSDKDomain(self, domain):
        pass

    def setSDKLanguage(self, language):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(language, str):
            if language in SDK_LANGUAGE:
                self.sdk_language = language
            else:
                self._is_error = True
                _state = False
        else:
            self._is_error = True
            _state = False
        return _state

    def setSDKAccent(self, accent):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(accent, str):
            if accent in SDK_ACCENT:
                self.sdk_accent = accent
            else:
                self._is_error = True
                _state = False
        else:
            self._is_error = True
            _state = False
        return _state

    def setSDKSampleRate(self, sampleRate):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(sampleRate, str):
            self.sdk_sample_rate = sampleRate
        elif isinstance(sampleRate, int):
            self.sdk_sample_rate = str(sampleRate)
        else:
            self._is_error = True
            _state = False
        return _state

    def setSDKPiceLen(self, piceLen):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(piceLen, str):
            self.sdk_pice_len = int(piceLen)
        elif isinstance(piceLen, int):
            self.sdk_pice_len = piceLen
        else:
            self._is_error = True
            _state = False
        return _state

    def is_error(self):
        return self._is_error

    def is_running(self):
        return self._is_running

    def is_web(self):
        return self._is_web

    def run(self):
        if self._is_error or self._is_running:
            return False
        self._is_running = True
        _state = True
        if self._is_web:
            try:
                fp = open(self.audio_path, 'rb')
            except :
                print('Open File Error!')
                fp.close()
                return False
            header = ISRHeader()
            header.SetEngineType(self.web_engine_type)
            header.UpdateParams()
            res = speech_to_text_web(header, fp)
            fp.close()
            return res
        else:
            try:
                fp = open(self.audio_path, 'rb')
            except Exception as e:
                print('Open File Error!')
                fp.close()
                return False

            params = {
                'sub': self.sdk_sub,
                'domain': self.sdk_domain,
                'language': self.sdk_language,
                'accent': self.sdk_accent,
                'sample_rate': self.sdk_sample_rate,
                'result_type': self.sdk_result_type,
                'result_encoding': self.sdk_result_encoding
            }
            isr = ISR()
            isrParam = ISRSessionParam()
            isrParam.params = params
            isr.setParams(isrParam.params)
            res = speech_to_text(isr, fp, piceLen=self.sdk_pice_len)
            fp.close()
            return res


