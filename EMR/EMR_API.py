"""
情感识别API，可直接调用进行情感识别
"""

from src.EMR.class_EMR import *


def emotion_recognition(emr):
    """
    情感识别API
    :param emr: EMR类，需在调用时进行设置
    :return: 情感识别结果(id, text)
    """
    return emr.GetResult()
