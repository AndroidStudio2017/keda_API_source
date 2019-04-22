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

        self.tmpStereoWave = './audio/tmpStereo.wav'
        self.tmpMonoWave = './audio/tmpMono.wav'
        self.outWave = './audio/test_out.wav'

        self.duration = '10'
        self.format = 'cd'
        self.sampleRate = '16000'
        self.channels = '1'
        self.fileType = 'wav'

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
        # generate raw audio
        rp = RecordParam()
        rp.SetAudioPath(self.tmpStereoWave)
        rp.params = paramDict
        record(rp)

        # generate Mono tmp
        print('Generate Mono audio ...')
        os.system('sox ' + self.tmpStereoWave + ' ' + self.tmpMonoWave + ' channels 1')
        print('Generate successfully: %s' % self.tmpMonoWave)

        # convert to 16kHz
        print("Convert to %skHz ..." % str(self.sampleRate))
        os.system('sox ' + self.tmpMonoWave + ' -r ' + self.sampleRate + ' ' + self.outWave)
        print('Audio in success!')
