"""
情感识别EMR类
"""

import ctypes
from src.EMR.class_EMR_param import *


class EMR:
    """
    EMR情感识别类
    """
    def __init__(self):
        """
        初始化EMR情感识别类参数
        """
        self.params = EMRParam()
        self.dll = ctypes.cdll.LoadLibrary('../libs/libemr.so')

    def SetAudioPath(self, path):
        """
        设置待识别音频路径
        :param path: 待识别音频路径
        :return: None
        """
        self.params.audioPath = path

    def SetResourceDir(self, path):
        """
        设置资源模型文件路径
        :param path: 资源模型文件路径
        :return: None
        """
        self.params.resourceDir = path

    def GetResult(self):
        """
        获取情感识别结果
        :return: 情感编号，情感文本
        """
        _EMR_recognition = self.dll.EMR_recognition
        emr_id = _EMR_recognition(self.params.audioPath)
        emr_text = self.params.table[emr_id]
        return emr_id, emr_text
