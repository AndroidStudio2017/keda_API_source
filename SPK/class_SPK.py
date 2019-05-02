"""

声纹识别SPK类
"""

import ctypes
from src.utils.utils import *


class SPK:
    """
    SPK声纹识别类
    """
    def __init__(self):
        self.dll = load_dll_msc('../libs/libwt.so')
        self.audioPath = './audio/test.wav'
        self.dataBuf = None
        self.dataLen = 0
        self.nDesiredNum = 5
        self.loadFlag = True

    def SetAudioPath(self, audioPath):
        """
        设置识别音频路径
        :param audioPath: 音频路径 str
        :return: None
        """
        self.loadFlag = True
        self.audioPath = audioPath

    def SetNDesiredNum(self, nDesiredNum):
        """
        设置期望的到的说话人识别数量
        :param nDesiredNum: 期望得到的说话人识别数量 int
        :return: None
        """
        self.nDesiredNum = nDesiredNum

    def GetDataLen(self):
        """
        获取音频长度
        :return: 音频长度 int
        """
        if self.dataLen == 0 or self.dataBuf is None:
            self.LoadWaveFile()
        return self.dataLen

    def LoadWaveFile(self):
        """
        加载音频文件 dll function
        :return: Success or fail
        """
        if not self.loadFlag:
            return True
        _LoadWaveFile = self.dll.LoadWaveFile
        _LoadWaveFile.argtypes = (ctypes.c_char_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_short)),
                                  ctypes.POINTER(ctypes.c_long))
        _LoadWaveFile.restype = ctypes.c_bool

        audioPath = get_c_char_p(self.audioPath)
        pDataBuf = ctypes.POINTER(ctypes.c_short)()
        dataLen = ctypes.c_long(0)
        _LoadWaveFile(audioPath, ctypes.byref(pDataBuf), ctypes.byref(dataLen))

        self.dataLen = dataLen
        self.dataBuf = pDataBuf

        if dataLen != 0:
            self.loadFlag = False
            return True
        else:
            return False

    def Recognize(self, offset, dataLen):
        """
        单次识别，从offset开始到offset + dataLen结束
        :param offset:      相对原音频的偏移
        :param dataLen:     识别的帧长度
        :return:
        """
        if self.dataLen == 0 or self.dataBuf is None:
            print('Audio is empty!')
            return False

        if not (isinstance(offset, int) and isinstance(dataLen, int)):
            print('Argument Type Error in SPK: ')
            print('offset ==> type(%s)' % type(offset))
            print('dataLen ==> type(%s)' % type(dataLen))
            return False

        _PyRecognize = self.dll.PyRecognize
        _PyRecognize.argtypes = (ctypes.POINTER(ctypes.c_short), ctypes.c_int, ctypes.c_int, ctypes.c_int)
        _PyRecognize.restype = ctypes.c_bool

        offset = ctypes.c_int(offset)
        dataLen = ctypes.c_int(dataLen)
        return _PyRecognize(self.dataBuf, offset, dataLen, self.nDesiredNum)

    def RecognizeAll(self, piceLen):
        """
        识别全部音频，以步长分开每次识别
        :param piceLen: 识别的步长 piceLen
        :return:
        """
        if self.dataLen == 0 or self.dataBuf is None:
            print('Audio is empty!')
            return False

        if not isinstance(piceLen, int):
            print('Argument Type Error in SPK: ')
            print('piceLen ==> type(%s)' % type(piceLen))
            return False

        _PyRecognizeAll = self.dll.PyRecognizeAll
        _PyRecognizeAll.argtypes = (ctypes.POINTER(ctypes.c_short), ctypes.c_int, ctypes.c_long, ctypes.c_int)
        _PyRecognizeAll.restype = ctypes.c_bool

        piceLen = ctypes.c_int(piceLen)
        return _PyRecognizeAll(self.dataBuf, piceLen, self.dataLen, self.nDesiredNum)
