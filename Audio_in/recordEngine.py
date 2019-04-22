from src.Audio_in.record_API import *
from src.Audio_in.class_record_param import *
from src.utils.utils import *


class recordEngine:
    """
    recordEngine类, 用于实现录音
    """

    def __init__(self):
        self._is_error = False
        self._is_running = False

        self.tmpWave = './audio/test.wav'
        self.outWave = './audio/test_out.wav'

        self.duration = '10'
        self.format = 'cd'
        self.sampleRate = '16000'
        self.channels = '1'
        self.fileType = 'wav'

    def SetTmpWave(self, tmpWave):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(tmpWave, str):
            self.tmpWave = tmpWave
        else:
            self._is_error = True
            _state = False
        return _state

    def SetOutWave(self, outWave):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(outWave, str):
            self.outWave = outWave
        else:
            self._is_error = True
            _state = False
        return _state

    def SetDuration(self, duration):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(duration, str):
            self.duration = duration
        elif isinstance(duration, int):
            self.duration = str(duration)
        else:
            self._is_error = True
            _state = False
        return _state

    def SetFormat(self, format):
        print('Warnning: It\'s not recommended to modify this argument.')
        pass

    def SetSampleRate(self, sampleRate):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(sampleRate, str):
            self.sampleRate = sampleRate
        elif isinstance(sampleRate, int):
            self.sampleRate = str(sampleRate)
        else:
            self._is_error = True
            _state = False
        return _state

    def SetChannels(self, channels):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(channels, str):
            self.channels = channels
        elif isinstance(channels, int):
            self.channels = str(channels)
        else:
            self._is_error = True
            _state = False
        return _state

    def SetFileType(self, fileType):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(fileType, str):
            self.fileType = fileType
        else:
            self._is_error = True
            _state = False
        return _state

    def run(self):
        if self._is_error or self._is_running:
            return False
        paramDict = {
            '-d': self.duration,
            '-f': self.format,
            '-r': self.sampleRate,
            '-c': self.channels,
            '-t': self.fileType
        }
        rp = RecordParam()
        rp.SetAudioPath(self.tmpWave)
        rp.params = paramDict
        record(rp)

        # downsample
        ds = DownSample()
        if not ds.open_file(self.tmpWave):
            print('Open %s Error.' % self.tmpWave)
            self._is_error = True
            return False

        ds.resample(self.outWave)
        return True
