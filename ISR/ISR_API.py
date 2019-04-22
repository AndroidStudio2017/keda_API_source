import requests
import time
import json

from src.ISR.ISR_SDK.class_ISR import *
from src.ISR.ISR_WEB.ISRHeader import *


def speech_to_text(isr, fp, piceLen):
    """
    将fp所指向的语音文件转化为文本
    :param isr: ISR类
    :param fp: 待转化文件句柄
    :param piceLen: 转化步长
    :return: 结果字符串
    """
    try:
        ret = isr.QISRSessionBegin()
        print(' QTTSSessionBegin => ret: ', ret, ' SessionID: ', isr.sessionID)
    except ISRException as e:
        print(' Get SessionID ERROR! ErrorCode: ', isr.ret)
        isr.MSPLogout()
        raise

    try:
        waveData = fp.read(piceLen)
        ret, epStatus, recogStatus = isr.QISRAudioWrite(waveData, piceLen, MSP_AUDIO_SAMPLE_FIRST)

        while waveData:
            waveData = fp.read(piceLen)

            if len(waveData) == 0:
                break
            ret, epStatus, recogStatus = isr.QISRAudioWrite(waveData, piceLen, MSP_AUDIO_SAMPLE_CONTINUE)
        isr.QISRAudioWrite(None, 0, MSP_AUDIO_SAMPLE_LAST)
    except ISRException as e:
        print(' Audio Write ERROR! ErrorCode: ', isr.ret)
        isr.MSPLogout()
        raise

    try:
        des_text = ''
        counter = 0
        while recogStatus != MSP_REC_STATUS_COMPLETE:
            text, ret, recogStatus = isr.QISRGetResult()
            if text is not None:
                des_text += text
            counter += 1
            time.sleep(0.1)
            counter += 1
            if counter == 500:
                des_text += '讯飞语音识别失败'
                break
    except ISRException as e:
        print(' Get Result ERROR! ErrorCode: ', isr.ret)
        isr.MSPLogout()
        raise

    ret = isr.QISRSessionEnd()
    return des_text


def speech_to_text_web(header, fp):
    """
    将fp所指向的语音文件转化为文本
    :param header: ISRHeader类
    :param fp: 待转化语音文件句柄
    :return: 识别结果字符串
    """
    data = {'audio': base64.b64encode(fp.read())}
    print('Recognizing...')
    r = requests.post(URL_ISR, headers=header.GetHeader(), data=data)
    r_json = json.loads(r.content.decode('utf-8'))
    if r_json['code'] == "0":
        print("Success in ISR.")
        # print(r.content.decode('utf-8'))
        return r_json['data']
    else:
        print("Fail in ISR")
        return r.content.decode('utf-8')
