# 应用参数定义
ADDID_LINUX = '5c935a75'
LOGIN_PARAM = 'appid = ' + ADDID_LINUX + ', work_dir = .'

# SDK语音合成部分常量定义
MSP_SUCCESS = 0
MSP_TTS_FLAG_DATA_END = 2

# SDK语音识别部分定义
MSP_SUCCESS = 0
MSP_AUDIO_SAMPLE_FIRST = 1
MSP_AUDIO_SAMPLE_CONTINUE = 2
MSP_AUDIO_SAMPLE_LAST = 4
MSP_REC_STATUS_COMPLETE = 5

FRAME_LEN = 640  # Byte

### This should be a configuration
# Web Engine Type
WEB_ENGINE_TYPE = ['sms16k', 'sms8k', 'sms-en8k', 'sms-en16k']
# SDK Language
SDK_LANGUAGE = ['zh_cn', 'en_us']
# SDK Accent
SDK_ACCENT = ['mandarin', 'cantonese', 'lmz']

# Web Services
APPID_WEB = '5ca549a7'

# Web TTS definitions
URL_TTS = "http://api.xfyun.cn/v1/service/v1/tts"
AUE_TTS = "raw"
API_KEY_TTS = "2d52ecc2e960550dd43e6ff3bcffbd49"

# Web ISR definitions
URL_ISR = "http://api.xfyun.cn/v1/service/v1/iat"
API_KEY_ISR = "ef790c78a3ce5d47eb5743734495906e"



