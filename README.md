# 科大讯飞语音识别和语音合成接口
## Overview
　　在官方提供的API中，只包含了c++实现的库文件，但Python作为目前的第一大编程语言，在科学计算领域已经有了很多的应用，在这里，我在科大讯飞提
供SDK的基础上，用Python进行封装，方便大家使用。
## 测试环境
- OS：Ubuntu 18.04 + 64位
- Python版本：3.7.0
- 保证网络环境

## 1. 语音识别接口(Linux SDK and WEB)
- ISR_SDK类：将与科大讯飞进行交互的各个动作封装成函数，如登录、会话建立等等，具体参见./ISR/class_ISR.py
- ISRSessionParam类：将会话建立所需参数封装成类，方便操作，具体参见./ISR/ISR_SDK/class_isrsession_param.py
- ISRException类：目前仅继承于Exception类
- ISRHeader类：用于组合和设置用于与科大讯飞API进行交互的请求头部，具体参见./ISR/ISR_WEB/ISRHeader.py
- ISRParams类：用于组合和设置用于与科大讯飞API进行交互的请求参数，具体参见./ISR/ISR_WEB/ISRParams.py
- ISR_API：如使用者不需要关心具体的C++调用实现，则可直接使用提供的API进行语音识别，具体参见./ISR/ISR_API.py
- ISREngine：语音识别引擎，用于完成语音识别所需的所有操作，具体参见./ISR/ISREngine.py
- demo：如若不懂API如何使用，可参见我编写的demo
## 2. 语音合成接口(Linux SDK and WEB)
- TTS_SDK类：将与科大讯飞进行交互的各个动作封装成函数，如登录、会话建立等等，具体参见./TTS/class_TTS.py
- TTSSessionParam类：将会话建立所需参数封装成类，方便操作，具体参见./TTS/TTS_SDK/class_ttssession_param.py
- TTSException类：目前仅继承于Exception类
- TTSHeader类：用于组合和设置用于与科大讯飞API进行交互的请求头部，具体参见./TTS/TTS_WEB/TTSHeader.py
- TTSParams类：用于组合和设置用于与科大讯飞API进行交互的请求参数，具体参见./TTS/TTS_WEB/TTSParams.py
- TTS_API：如使用者不需要关心具体的C++调用实现，则可直接使用提供的API进行语音识别，具体参见./TTS/TTS_API.py
- TTSEngine：语音合成引擎，用于完成语音合成所需的所有操作，具体参见./TTS/TTSEngine.py
- demo：如若不懂API如何使用，可参见我编写的demo
## 3. 情感识别接口(自己实现)
- EMR类：将修改参数等接口暴露，提供GetResult函数直接获取识别结果，具体参见./EMR/class_EMR.py
- EMRParam类：将EMR参数封装，方便EMR调用，同时进行一些错误控制，具体参见./EMR/class_EMR_param.py
- EMR_API类：向外提供的情感识别接口，**在调用之前必须设置识别音频路径！！**，具体参见./EMR/EMR_API.py
- EMREngine类：情感识别引擎，用于完成情感识别所需的所有操作，具体参见./EMR/EMREngine.py
- demo类：如若不懂如何使用API，可参见我编写的demo
## 4. 声纹识别接口(自己实现)
- SPK类：将修改参数等接口暴露，提供Recognize函数和RecognizeAll函数直接获取识别结果，具体参见./SPK/class_SPK.py
- SPKEngine类： 声纹识别引擎，用于完成声纹识别所需的所有操作，具体参见./SPK/class_SPK.py
- demo类：如若不懂如何使用Engine，可参见我编写的demo
## 5. Linux音频输入接口(录音)
- RecordParam类：将录音所需参数封装成类，向外提供修改录音文件保存位置的接口.具体参见./Audio_in/class_record_param.py
- record_API：利用Linux系统命令控制默认录音设备进行录音.具体参见./Audio_in/record_API.py
- demo：如若不懂如何使用API，可参见我编写的简易demo
## 6. Linux音频输出接口(播放)
- PlayParam类：将播放所需参数封装成类，向外提供修改播放文件路径的接口，具体参见./Audio_out/class_play_param.py
- play_API：利用Linux系统命令控制默认输出设备进行播放，具体参见./Audio_out/play_API.py
- demo：如若不懂如何使用API，可参见我编写的简易demo
## 7. 语音天气播报
- config.json：语音播报的json配置文件，可用于更改一些配置.目前实现可更改城市名称，后续增加更多可配置内容.详情见./Weather_research/config.json
- Weather.py：实现爬取中国天气网上的天气内容，并返回相应的播报数据.详见./Weather_research/demo.py
- demo.py：用于实现完整的语音播报功能.详见./Weather_research/demo.py

**To be continued...**
