"""

定义了 TTS类, 封装了用于语音合成的一系列函数.

"""
from src.utils.utils import *
from src.utils.define import *
from src.TTS.TTS_SDK.class_ttssession_param import *
from src.TTS.TTS_SDK.class_TTSException import *


class TTS:
    """

    TTS 语音合成类, 包含与科大讯飞进行语音合成交互的各种动作.

    """
    login = {
        'logined': False,
        'usr': None,
        'pwd': None,
        'params': LOGIN_PARAM
    }
    # 音频参数 nchannels, sampwidth, framerate, nframes, comptype, compname
    wav_params = [1, 2, 16000, 0, 'NONE', 'not compressed']

    def __init__(self, ):
        self.dll = load_dll_msc('../libs/libmsc.so')

        self.sessionID = None
        self.sessionend_hints = 'Normal'
        self.ret = MSP_SUCCESS
        self.session_begin_params_obj = TTSSessionParam()
        self.session_begin_params = self.session_begin_params_obj.params

    def UpdateParams(self):
        """
        修改完参数后需要进行Update, 使设置生效
        :return: None
        """
        self.session_begin_params = self.session_begin_params_obj.params

    def SetSampleRate(self, sampleRate):
        """
        设置合成音频采样率, 具体需要查看文档
        :param sampleRate: 采样率
        :return: Success or Fail
        """
        if self.session_begin_params_obj.SetSampleRate(sampleRate):
            self.wav_params[2] = int(sampleRate)
            return True
        return False

    def SetVoiceByName(self, voiceName):
        """
        设置合成声音, 具体需要查看文档
        :param voiceName: 声音名字
        :return: Success or Fail
        """
        if self.session_begin_params_obj.SetVoiceByName(voiceName):
            return True
        return False

    def SetSpeed(self, speed):
        """
        设置合成声音语速
        :param speed: int 语速 0~100 or str
        :return: Success or fail
        """
        if(self.session_begin_params_obj.SetSpeed(speed)):
            return True
        return False

    def SetVolume(self, volume):
        """
        设置合成声音大小
        :param volume: int 声音大小 0~100 or str
        :return: Success or fail
        """
        if(self.session_begin_params_obj.SetVolume(volume)):
            return True
        return False

    def SetPitch(self, pitch):
        """
        设置合成声音语调
        :param pitch: int 声音语调 0~100 or str
        :return: Success or fail
        """
        if(self.session_begin_params_obj.SetPitch(pitch)):
            return True
        return False

    def MSPLogin(self):
        """
        /**
         * @fn		MSPLogin
         * @brief	user login interface
         *
         *  User login.
         *
         * @return	int MSPAPI			- Return 0 in success, otherwise return error code.
         * @param	const char* usr		- [in] user name.
         * @param	const char* pwd		- [in] password.
         * @param	const char* params	- [in] parameters when user login.
         * @see
         */
        int MSPAPI MSPLogin(const char* usr, const char* pwd, const char* params);
        """
        assert self.dll is not None, 'Please load msx_64.dll, Before load this function'

        _MSPLogin = self.dll.MSPLogin
        _MSPLogin.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p)
        _MSPLogin.restype = ctypes.c_int

        c_usr = get_c_char_p(self.login['usr'])
        c_pwd = get_c_char_p(self.login['pwd'])
        c_params = get_c_char_p(self.login['params'])
        ret = _MSPLogin(c_usr, c_pwd, c_params)

        if MSP_SUCCESS != ret:
            raise TTSException('MSPLogin failed, error code: %d.' % (ret))

        if MSP_SUCCESS == ret:
            self.login['logined'] = True

        return ret

    def MSPLogout(self):
        """
        /**
         * @fn		MSPLogout
         * @brief	user logout interface
         *
         *  User logout
         *
         * @return	int MSPAPI			- Return 0 in success, otherwise return error code.
         * @see
         */
        int MSPAPI MSPLogout();
        """

        _MSPLogout = self.dll.MSPLogout
        _MSPLogout.argtypes = ()
        _MSPLogout.restype = ctypes.c_int

        ret = _MSPLogout()
        self.login['logined'] = False

        return ret

    def SetWaveParam(self, nchannels=1, sampwidth=2, framerate=16000, nframes=0, comptype='None', compname='not compressed'):
        """
        设置音频参数
        :param nchannels: 信道     默认为 1
        :param sampwidth: 采样宽度 默认为 2bit
        :param framerate: 采样率   默认为 16000kHz
        :param nframes:   一般为默认值即可
        :param comptype:  一般为默认值即可
        :param compname:  一般为默认值即可
        :return: None
        """
        self.wav_params = (nchannels, sampwidth, framerate, nframes, comptype, compname)

    def QTTSSessionBegin(self, params=None):
        """
        /**
         * @fn		QTTSSessionBegin
         * @brief	Begin a TTS Session
         *
         *  Create a tts session to synthesize data.
         *
         * @return	const char* - Return the new session id in success, otherwise return NULL, error code.
         * @param	const char* params			- [in] parameters when the session created.
         * @param	int* errorCode				- [out] error code if failed, 0 to success.
         * @see
         */
        const char* MSPAPI QTTSSessionBegin(const char* params, int* errorCode);
        """
        # 检查登录状态
        if self.login['logined'] is False:
            self.MSPLogin()

        # 检测会话参数设置
        if params is not None:
            self.session_begin_params = params
        else:
            params = self.session_begin_params

        _QTTSSessionBegin = self.dll.QTTSSessionBegin
        _QTTSSessionBegin.argtypes = (ctypes.c_char_p, ctypes.POINTER(ctypes.c_int))
        _QTTSSessionBegin.restype = ctypes.c_char_p

        c_params = get_c_char_p(params)
        c_errorCode = ctypes.c_int()
        sessionID = _QTTSSessionBegin(c_params, c_errorCode)
        if sessionID is not None:
            self.sessionID = sessionID.decode('utf-8')

        ret = c_errorCode.value
        self.ret = ret
        if ret != MSP_SUCCESS:
            self.MSPLogout()
            raise TTSException('QTTSSessionBegin failed, error code: %d' % (ret))

        return ret

    def QTTSSessionEnd(self):
        """
        /**
         * @fn		QTTSSessionEnd
         * @brief	End a Recognizer Session
         *
         *  End the recognizer session, release all resource.
         *
         * @return	int MSPAPI	- Return 0 in success, otherwise return error code.
         * @param	const char* session_id	- [in] session id string to end
         * @param	const char* hints	- [in] user hints to end session, hints will be logged to CallLog
         * @see
         */
        int MSPAPI QTTSSessionEnd(const char* sessionID, const char* hints);
        """
        # 检查sessionID状态
        assert self.sessionID is not None, 'seesionId is None,Please call QTTSSessionBegin defore QTTSSessionEnd called'

        _QTTSSessionEnd = self.dll.QTTSSessionEnd
        _QTTSSessionEnd.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
        _QTTSSessionEnd.restype = ctypes.c_int

        c_sessionID = get_c_char_p(self.sessionID)
        c_hints = get_c_char_p(self.sessionend_hints)

        ret = _QTTSSessionEnd(c_sessionID, c_hints)
        self.ret = ret

        return ret

    def QTTSTextPut(self, textString, params):
        '''
        /**
         * @fn		QTTSTextPut
         * @brief	Put Text Buffer to TTS Session
         *
         *  Writing text string to synthesizer.
         *
         * @return	int MSPAPI	- Return 0 in success, otherwise return error code.
         * @param	const char* sessionID	- [in] The session id returned by sesson begin
         * @param	const char* textString	- [in] text buffer
         * @param	unsigned int textLen	- [in] text size in bytes
         * @see
         */
        int MSPAPI QTTSTextPut(const char* sessionID, const char* textString, unsigned int textLen, const char* params);
        '''
        # 检查sessionID状态
        assert self.sessionID is not None, 'seesionId is None,Please call QTTSSessionBegin defore QTTSTextPut called'

        _QTTSTextPut = self.dll.QTTSTextPut
        _QTTSTextPut.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p)
        _QTTSTextPut.restype = ctypes.c_int

        c_seesionID = get_c_char_p(self.sessionID)
        text = textString.encode('utf-8')
        c_textString = get_c_char_p(text)
        c_textLen = ctypes.c_int(len(text))
        c_params = get_c_char_p(params)

        ret = _QTTSTextPut(c_seesionID, c_textString, c_textLen, c_params)
        self.ret = ret

        return ret

    def QTTSAudioGet(self):
        '''
        /**
         * @fn		QTTSAudioGet
         * @brief	Synthesize text to audio
         *
         *  Synthesize text to audio, and return audio information.
         *
         * @return	const void*	- Return current synthesized audio data buffer, size returned by QTTSTextSynth.
         * @param	const char* sessionID	- [in] session id returned by session begin
         * @param	unsigned int* audioLen 	- [out] synthesized audio size in bytes
         * @param	int* synthStatus	- [out] synthesizing status
         * @param	int* errorCode	- [out] error code if failed, 0 to success.
         * @see
         */
        const void* MSPAPI QTTSAudioGet(const char* sessionID, unsigned int* audioLen, int* synthStatus, int* errorCode);
        '''
        # 检查sessionID状态
        assert self.sessionID is not None, 'seesionId is None,Please call QTTSSessionBegin defore QTTSAudioGet called'

        _QTTSAudioGet = self.dll.QTTSAudioGet
        _QTTSAudioGet.argtypes = (
            ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
        _QTTSAudioGet.restype = ctypes.c_void_p

        c_seesionID = get_c_char_p(self.sessionID)
        c_audioLen = ctypes.c_int()
        c_synthStatus = ctypes.c_int()
        c_errorCode = ctypes.c_int()

        ptr_data = _QTTSAudioGet(c_seesionID, c_audioLen, c_synthStatus, c_errorCode)
        self.ret = c_errorCode.value

        return c_audioLen.value, c_synthStatus.value, c_errorCode.value, ptr_data

    def __enter__(self):
        # self.MSPLogin()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.MSPLogout()
        pass
