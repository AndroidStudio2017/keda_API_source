from src.SPK.class_SPK import *
from src.SPK.SPK_API import *


class SPKEngine:
    """
    声纹识别引擎类SPKEngine
    """
    def __init__(self):
        self._is_error = False
        self._is_running = False
        self._is_once = False

        self.audioPath = './audio/test.wav'
        self.nDesiredNum = 5

        # once
        self.offset = 0
        self.dataLen = 16000

        # all
        self.piceLen = 16000

    def SetOffset(self, offset):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(offset, int):
            self.offset = offset
        elif isinstance(offset, str):
            self.offset = int(offset)
        else:
            self._is_error = True
            _state = False
        return _state

    def SetDataLen(self, dataLen):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(dataLen, int):
            self.dataLen = dataLen
        elif isinstance(dataLen, str):
            self.dataLen = int(dataLen)
        else:
            self._is_error = True
            _state = False
        return _state

    def SetPiceLen(self, piceLen):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(piceLen, int):
            self.piceLen = piceLen
        elif isinstance(piceLen, str):
            self.piceLen = int(piceLen)
        else:
            self._is_error = True
            _state = False
        return _state

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

    def SetNDesiredNum(self, nDesiredNum):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(nDesiredNum, int):
            self.nDesiredNum = nDesiredNum
        elif isinstance(nDesiredNum, str):
            self.nDesiredNum = int(nDesiredNum)
        else:
            self._is_error = True
            _state = False
        return _state

    def SetWorkType(self, workType):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(workType, str):
            if workType == 'all':
                self._is_once = False
            elif workType == 'once':
                self._is_once = True
            else:
                self._is_error = True
                _state = False
        else:
            self._is_error = True
            _state = False
        return _state

    def run(self):
        if self._is_error or self._is_running:
            return False
        self._is_running = True
        _state = True
        spk = SPK()
        spk.SetAudioPath(self.audioPath)
        spk.SetNDesiredNum(self.nDesiredNum)
        spk.LoadWaveFile()
        if self._is_once:
            _state = spk.Recognize(self.offset, self.dataLen)
        else:
            _state = spk.RecognizeAll(self.piceLen)
        return _state
