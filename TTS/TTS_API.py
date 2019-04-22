import time
import requests

from src.TTS.TTS_SDK.class_TTS import *
from src.TTS.TTS_WEB.TTSHeader import *

def text_to_speech(tts, fp, src_text):
    """
    将文本转化为语音, 转存入fp指向的文件中
    :param tts: TTS语音合成对象
    :param fp: 写入的文件句柄
    :param src_text: 待转化的文字
    :return: None
    """
    # 设置fp写入参数  设置三个主要参数足以
    fp.setnchannels(tts.wav_params[0])
    fp.setsampwidth(tts.wav_params[1])
    fp.setframerate(tts.wav_params[2])

    if not isinstance(src_text, str):
        raise ValueError("expect <class 'str'>,value:{!r}, got{}".format(src_text, type(src_text)))

    try:
        ret = tts.QTTSSessionBegin()
        print(' QTTSSessionBegin => ret: ', ret, ' SessionID: ', tts.sessionID)
    except TTSException as e:
        print(' Get SessionID ERROR! ErrorCode: ', tts.ret)
        tts.MSPLogout()
        raise
    try:
        ret = tts.QTTSTextPut(src_text, None)
        print(' QTTSTextPut => ret: ', ret)
        if ret != MSP_SUCCESS:
            tts.sessionend_hints = 'TextPutError'
            raise TTSException('QTTSTextPut failed, error code: %d' % (ret))

        while True:
            audioLen, synthStatus, ret, ptr = tts.QTTSAudioGet()
            print(' audioLen: ', audioLen, 'synthStatus: ', synthStatus, 'ret: ', ret, 'ptr: ', ptr)
            if MSP_SUCCESS != ret:
                break
            if ptr is not None:
                d = ctypes.string_at(ptr, audioLen)
                fp.writeframes(d)
            if MSP_TTS_FLAG_DATA_END == synthStatus:
                break
            time.sleep(0.1)
        if ret != MSP_SUCCESS:
            tts.sessionend_hints = 'AudioGetError'
            raise TTSException('QTTSAudioGet failed, error code: %d.' % (ret))
    except TTSException as e:
        raise
    finally:
        tts.QTTSSessionEnd()


def text_to_speech_web(header, fp, src_text):
    """
    将文本转化为语音, 转存入fp指向的文件中
    :param header: Post Header 用于向云发送请求，具体见TTSHeader
    :param fp: 要写入的文件句柄, 二进制
    :param src_text: 待转化的文字
    :return: None
    """
    data = {'text': src_text}
    r = requests.post(URL_TTS, headers=header.GetHeader(), data=data)
    contentType = r.headers['Content-Type']

    if contentType == "audio/mpeg":
        sid = r.headers['sid']
        print('Writing to ' + fp.name + '...')
        fp.write(r.content)

        print("success, sid = " + sid)
    else:
        print(r.text)
