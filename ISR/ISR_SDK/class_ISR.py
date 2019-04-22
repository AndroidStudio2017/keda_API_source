"""

定义了 ISR类, 封装了用于语音合成的一系列函数.

"""
from src.utils.utils import *
from src.utils.define import *
from src.ISR.ISR_SDK.class_isrsession_param import *
from src.ISR.ISR_SDK.class_ISRException import *


class ISR:
    """

    ISR 语音识别类, 包含与科大讯飞进行语音识别交互的各种动作.

    """
    login = {
        'logined': False,
        'usr': None,
        'pwd': None,
        'params': LOGIN_PARAM
    }

    def __init__(self):
        self.dll = load_dll_msc('../libs/libmsc.so')
        self.sessionID = None
        self.sessionend_hints = 'Normal'
        self.ret = MSP_SUCCESS
        self.session_begin_params = ISRSessionParam().params

    def setParams(self, Param):
        self.session_begin_params = Param
        return True

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

        assert self.dll is not None, 'Please load libmsc.dll, Before load this function'

        _MSPLogin = self.dll.MSPLogin
        _MSPLogin.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p)
        _MSPLogin.restype = (ctypes.c_int)

        c_usr = get_c_char_p(self.login['usr'])
        c_pwd = get_c_char_p(self.login['pwd'])
        c_params = get_c_char_p(self.login['params'])
        ret = _MSPLogin(c_usr, c_pwd, c_params)

        if ret != MSP_SUCCESS:
            raise ISRException('MSPLogin failed, error code: %d.' % (ret))

        if ret == MSP_SUCCESS:
            self.ret = ret
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

        assert self.dll is not None, 'Please load libmsc.dll, Before load this function'

        _MSPLogout = self.dll.MSPLogout
        _MSPLogout.argtypes = ()
        _MSPLogout.restype = (ctypes.c_int)

        ret = _MSPLogout()
        self.login['logined'] = False
        self.ret = ret

        return ret

    def QISRSessionBegin(self, params=None):
        """
        /**
         * @fn		QISRSessionBegin
         * @brief	Begin a ISR Session
         *
         *  Create a ISR Session
         *
         * @return	const char* - Return the new session id in success, otherwise return NULL
         * @param   const char*                 - [in]  grammarList, always NULL
         * @param   const char*                 - [in]  parameters when the session created.
         * @param	int* errorCode				- [out] error code if failed, 0 to success.
         * @see
         */
        const char* MSPAPI QISRSessionBegin	(const char *grammarList, const char *params, int *errorCode)
        """
        # 检查登录状态
        if self.login['logined'] is False:
            self.MSPLogin()

        # 检测会话参数设置
        if params is not None:
            self.session_begin_params = params
        else:
            params = self.session_begin_params

        _QISRSessionBegin = self.dll.QISRSessionBegin
        _QISRSessionBegin.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int)
        _QISRSessionBegin.restype = ctypes.c_char_p

        c_grammarList = None
        c_params = get_c_char_p(params)
        c_errorCode = ctypes.c_int()
        sessionID = _QISRSessionBegin(c_grammarList, c_params, c_errorCode)

        if sessionID is not None:
            self.sessionID = sessionID.decode('utf8')

        ret = c_errorCode.value
        self.ret = ret
        if ret != MSP_SUCCESS:
            self.MSPLogout()
            raise ISRException('QISRSessionBegin failed, error code: %d' % (ret))

        return ret

    def QISRSessionEnd(self):
        """
        /**
         * @fn		QISRSessionEnd
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

        _QISRSessionEnd = self.dll.QISRSessionEnd
        _QISRSessionEnd.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
        _QISRSessionEnd.restype = ctypes.c_int

        c_sessionID = get_c_char_p(self.sessionID)
        c_hints = get_c_char_p(self.sessionend_hints)

        ret = _QISRSessionEnd(c_sessionID, c_hints)
        self.ret = ret

        return ret

    def QISRAudioWrite(self, waveData, waveLen, audioStatus):
        """
        /**
         * @fn		QISRAudioWrite
         * @brief	Write audio data to server
         *
         *  Start to write audio data
         *
         * @return	int - Return error code if failed, 0 to success.
         * @param   const char*                 - [in]  sessionID which used to keep alive
         * @param   const void*                 - [in]  audio data
         * @param   unsigned int                - [in]  data length in one time
         * @param   int                         - [out] audio status
                                                        1: the first block of audio data
                                                        2: there are some audio data behind
                                                        3: the last block of audio data
         * @param	int*        				- [out] epStatus
                                                        0: looking for speech
                                                        1: processing speech
                                                        3: finished
                                                        4: timeout
                                                        5: error
                                                        6: audio data is too large
         * @param   int*                        - [out] recogStatus
                                                        0: recognize successfully
                                                        1: no match
                                                        2: recognizing
                                                        5: finished
         * @see
         */
        int MSPAPI QISRAudioWrite(const char *sessionID, const void *waveData, unsigned int waveLen,
                        int audioStatus, int *epStatus, int *recogStatus)
        """

        # 检查sessionID状态
        assert self.sessionID is not None, 'seesionId is None,Please call QISRSessionBegin defore QTTSSessionEnd called'

        _QISRAudioWrite = self.dll.QISRAudioWrite
        _QISRAudioWrite.argtypes = (ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int,
                                    ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
        _QISRAudioWrite.restypes = (ctypes.c_int)

        c_sessionID = get_c_char_p(self.sessionID)
        c_epStatus = ctypes.c_int()
        c_recogStatus = ctypes.c_int()

        ret = _QISRAudioWrite(c_sessionID, waveData, waveLen, audioStatus, c_epStatus, c_recogStatus)
        self.ret = ret

        if ret != MSP_SUCCESS:
            self.MSPLogout()
            raise ISRException('QISRAudioWrite failed, error code: %d' % (ret))

        return ret, c_epStatus.value, c_recogStatus.value

    def QISRGetResult(self):
        """
        /**
         * @fn		QISRGetResult
         * @brief	Get the text of the audio data
         *
         *  Get the text of the audio data from website
         *
         * @return	const char* - Return the recognition result
         * @param   const char*                 - [in]  sessionID which used to keep alive
         * @param   int*                        - [out] the status of result
                                                    0: recognize successfully
                                                    1: no match
                                                    2: recognizing
                                                    5: finished
         * @param   int                         - [in]  no use, make it 0
         * @param	int* errorCode				- [out] error code if failed, 0 to success.
         * @see
         */
         const char* MSPAPI QISRGetResult(const char *sessionID, int *rsltStatus, int waitTime, int *errorCode)
        """
        # 检查sessionID状态
        assert self.sessionID is not None, 'seesionId is None,Please call QISRSessionBegin defore QTTSSessionEnd called'

        _QISRGetResult = self.dll.QISRGetResult
        _QISRGetResult.argtypes = (ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.POINTER(ctypes.c_int))
        _QISRGetResult.restype = ctypes.c_char_p

        c_sessionID = get_c_char_p(self.sessionID)
        c_rsltStatus = ctypes.c_int()
        c_waitTime = ctypes.c_int(0)
        c_errorCode = ctypes.c_int()

        bstr = _QISRGetResult(c_sessionID, c_rsltStatus, c_waitTime, c_errorCode)
        if bstr is not None:
            string = str(bstr, encoding='utf8')
        else:
            string = ''

        ret = c_errorCode.value
        self.ret = ret
        if ret != MSP_SUCCESS:
            self.MSPLogout()
            raise ISRException('QISRGetResult failed, error code: %d' % (ret))

        return string, ret, c_rsltStatus.value

    def __enter__(self):
        # self.MSPLogin()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.MSPLogout()
        pass
