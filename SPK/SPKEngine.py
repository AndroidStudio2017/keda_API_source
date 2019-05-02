import sys
sys.path.append('../../')

from src.SPK.class_SPK import *


class SPKEngine:
    """
    声纹识别引擎类SPKEngine
    """
    def __init__(self):
        """
        初始化参数
        """
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
        """
        设置偏移量接口
        :param offset:  偏移量
        :return: Success or Fail
        """
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
        """
        设置单次识别数据长度
        :param dataLen: 识别数据长度
        :return: Success or Fail
        """
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
        """
        设置识别步长
        :param piceLen: 步长
        :return: Success or Fail
        """
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
        """
        设置识别音频路径
        :param audioPath: 音频路径
        :return: Success or Fail
        """
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
        """
        设置渴望得到的识别说话人数量
        :param nDesiredNum: 说话人数量
        :return: Success or Fail
        """
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
        """
        设置工作类型(all, once)
        :param workType: 工作类型
        :return: Success or Fail
        """
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
        """
        根据设置参数运行
        :return: Success or Fail
        """
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
