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

    def SetAudioPath(self, audioPath):
        """

        :param audioPath:
        :return:
        """
        self.audioPath = audioPath

    def SetNDesiredNum(self, nDesiredNum):
        """

        :param nDesiredNum:
        :return:
        """
        self.nDesiredNum = nDesiredNum

    def GetDataLen(self):
        """

        :return:
        """
        return self.dataLen

    def LoadWaveFile(self):
        """

        :param szWaveName:
        :param pDataBuf:
        :param dataLen:
        :return:
        """
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
            return True
        else:
            return False

    def Recognize(self, offset, dataLen):
        """

        :param offset:
        :param dataLen:
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

        :param piceLen:
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
