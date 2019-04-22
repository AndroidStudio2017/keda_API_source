"""

定义TTSHeader类，方便进行Header参数处理

"""

#-*- coding: utf-8 -*-
import time
import hashlib
import base64

from src.utils.utils import *
from src.utils.define import *
from src.TTS.TTS_WEB.TTSParams import *


class TTSHeader:
    """
    用于发送TTS Post请求的Header
    """

    def __init__(self):
        """
        初始化默认参数
        """
        self.curTime = str(int(time.time()))
        self.Param = TTSParams()
        self.ParamBase64 = ''
        self.m2 = hashlib.md5()
        self.checkSum = ''
        self.Content_Type = 'application/x-www-form-urlencoded; charset=utf-8'

    def UpdateParams(self):
        """
        修改完参数后需要进行Update, 使设置生效
        :return: None
        """
        self.GetParamBase64()
        self.GetCheckSum()

    def SetAuf(self, auf):
        if self.Param.SetAuf(auf):
            return True
        return False

    def SetAue(self, aue):
        if self.Param.SetAue(aue):
            return True
        return False

    def SetEngineType(self, engineType):
        if self.Param.SetEngineType(engineType):
            return True
        return False

    def SetText(self, text):
        if self.Param.SetText(text):
            return True
        return False

    def SetVoiceByName(self, voiceName):
        """
        设置合成声音, 具体需要查看文档
        :param voiceName: 声音名字
        :return: None
        """
        if(self.Param.SetVoiceByName(voiceName)):
            return True
        return False

    def SetSpeed(self, speed):
        """
        设置合成声音语速
        :param speed: int 语速 0~100 or str
        :return: Success or fail
        """
        if(self.Param.SetSpeed(speed)):
            return True
        return False

    def SetVolume(self, volume):
        """
        设置合成声音大小
        :param volume: int 声音大小 0~100 or str
        :return: Success or fail
        """
        if(self.Param.SetVolume(volume)):
            return True
        return False

    def SetPitch(self, pitch):
        """
        设置合成声音语调
        :param pitch: int 声音语调 0~100 or str
        :return: Success or fail
        """
        if(self.Param.SetPitch(pitch)):
            return True
        return False

    def GetParamBase64(self):
        """
        得到Base64编码的Param
        :return: ParamBase64, Base64编码的Param 可直接用于Header
        """

        assert self.Param is not None
        self.ParamBase64 = str(base64.b64encode(self.Param.Params.encode('utf-8')), 'utf-8')
        return self.ParamBase64

    def GetCheckSum(self):
        """
        得到校验和
        :return: 校验和，可直接用于Header
        """

        assert self.curTime is not None and self.ParamBase64 is not None
        self.m2 = hashlib.md5()
        self.m2.update((API_KEY_TTS + self.curTime + self.ParamBase64).encode('utf-8'))

        self.checkSum = self.m2.hexdigest()
        return self.checkSum


    def GetHeader(self):
        header = {}
        header['X-CurTime'] = self.curTime
        header['X-Param'] = self.ParamBase64
        header['X-Appid'] = APPID_WEB
        header['X-CheckSum'] = self.checkSum
        header['X-Real-Ip'] = '127.0.0.1'
        header['Content-Type'] = self.Content_Type
        return header
