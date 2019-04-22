import wave

from src.TTS.TTS_API import *


class TTSEngine:
    """
    TTSEngine类，用于实现TTS
    """
    def __init__(self):
        self._is_running = False
        self._is_error = False
        self._is_web = False

        self.src_text = '这是系统默认的合成语句'
        self.audioPath = './wav_output/test.wav'
        self.speed = '50'
        self.volume = '50'
        self.pitch = '50'
        self.voice_name = 'xiaoyan'

        self.sdk_text_encoding = 'utf8'
        self.sdk_sample_rate = '16000'
        self.sdk_rdn = '2'

        self.web_auf = 'audio/L16;rate=16000'
        self.web_aue = 'raw'
        self.web_engine_type = 'intp65'
        self.web_text = 'text'

    def is_error(self):
        return self._is_error

    def is_running(self):
        return self._is_running

    def is_web(self):
        return self._is_web

    def SetAudioPath(self, audioPath):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(audioPath, str):
            self.audioPath = audioPath
        else:
            self._is_error = True
            _state = False
        return _state

    def SetEngine(self, engine):
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

    def SetSrcText(self, src_text):
        if self._is_error or self._is_running:
            return False
        _state = True
        try:
            self.src_text = str(src_text)
        except Exception as e:
            print('src_text has a error type: ', type(src_text))
            self._is_error = True
            _state = False
        return _state

    def SetSpeed(self, speed):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(speed, str):
            self.speed = speed
        elif isinstance(speed, int):
            self.speed = str(speed)
        else:
            self._is_error = True
            _state = False
        return _state

    def SetVolume(self, volume):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(volume, str):
            self.volume = volume
        elif isinstance(volume, int):
            self.volume = str(volume)
        else:
            self._is_error = True
            _state = False
        return _state

    def SetPitch(self, pitch):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(pitch,str):
            self.pitch = pitch
        elif isinstance(pitch, int):
            self.pitch = str(pitch)
        else:
            self._is_error = True
            _state = False
        return _state

    def SetVoiceName(self, voiceName):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(voiceName, str):
            self.voice_name = voiceName
        else:
            self._is_error = True
            _state = False
        return _state

    def SetSDKSampleRate(self, sampleRate):
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

    def run(self):
        if self._is_error or self._is_running:
            return False
        _state = True

        if self._is_web:
            header = TTSHeader()
            header.SetVoiceByName(self.voice_name)
            header.SetVolume(self.volume)
            header.SetSpeed(self.speed)
            header.SetPitch(self.pitch)
            header.SetAuf(self.web_auf)
            header.SetAue(self.web_aue)
            header.SetText(self.web_text)
            header.SetEngineType(self.web_engine_type)
            header.UpdateParams()
            fp = open(self.audioPath, 'wb')
            text_to_speech_web(header, fp, self.src_text)
            fp.close()
        else:
            tts = TTS()
            tts.SetVoiceByName(self.voice_name)
            tts.SetVolume(self.volume)
            tts.SetSpeed(self.speed)
            tts.SetPitch(self.pitch)
            tts.SetSampleRate(self.sdk_sample_rate)
            tts.UpdateParams()
            fp = wave.open(self.audioPath, 'wb')
            text_to_speech(tts, fp, self.src_text)
            fp.close()

        print('Success in TTS!')
