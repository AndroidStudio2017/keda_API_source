import sys
sys.path.append('../../')

import json
from src.ISR.ISR_API import *
from src.TTS.TTS_API import *
from src.Weather_research.Weather import *
from src.Audio_in.record_API import *
from src.Audio_in.class_record_param import *
from src.Audio_out.class_play_param import *
from src.Audio_out.play_API import *


def _ISR(filepath):
    """
    调用ISR_API接口进行语音识别，方法同ISR/demo.py
    :param filepath: 待识别语音文件路径
    :return: 识别结果 str
    """
    fp = open(filepath, 'rb')
    header = ISRHeader()
    header.UpdateParams()
    res = speech_to_text_web(header, fp)
    fp.close()
    return res


def _TTS(text):
    """
    调用TTS模块合成语音
    :param text: 带合成天气结果文本
    :return: None
    """
    testStr = text
    filepath = './wav_output/output.wav'
    header = TTSHeader()
    header.SetVoiceByName('aisbabyxu')
    header.UpdateParams()
    fp = open(filepath, 'wb')
    text_to_speech_web(header, fp, testStr)
    fp.close()


def Audio_in():
    """
    录音函数，同Audio_in/demo.py
    :return: None
    """
    rp = RecordParam()
    rp.SetAudioPath('./wav_output/input.wav')
    record(rp)


def Audio_out(filepath):
    """
    放音函数，同Audio_out/demo.py
    :param filepath: 待播放的音频文件路径
    :return: None
    """
    pp = PlayParam()
    pp.params = filepath
    play(pp)


def main():
    """
    完整的天气播报功能
    :return: None
    """
    with open('./config.json', 'r') as fp:          # Load Configuration
        config = json.load(fp)
    # print(config)

    Audio_out('./indicate.wav')
    Audio_in()
    text = str(_ISR('./wav_output/input.wav'))
    print("识别输入结果: ", text)

    # text = "北京今天的天气是啥"
    speech = "请重新再说一遍"
    print('正在从中国天气网获取今日天气数据 ...')
    if "天气" in text:
        for i in config['city_list']:
            if i in text:
                speech = weather_report(i)
                break
    print('天气数据获取完毕!')
    print('正在进行语音合成 ...')
    _TTS(speech)
    print(speech)
    Audio_out('./wav_output/output.wav')


if __name__ == '__main__':
    main()


