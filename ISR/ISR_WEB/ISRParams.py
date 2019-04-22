"""

定义了ISRParams类, 封装了Web语音识别参数

"""
from collections import OrderedDict


class ISRParams:
    """
    Web语音合成参数类
    """

    def __init__(self):
        """
        初始化默认参数
        """
        self._ISRParams = OrderedDict()
        self._ISRParams['aue'] = 'raw'
        #self._ISRsession_begin_paramsParams['speex_size'] = '60'
        #self._ISRParams['scene'] = 'main'
        #self._ISRParams['vad_eos'] = '2000'
        self._ISRParams['engine_type'] = 'sms16k'

    def SetEngineType(self, engineType):
        """
        设置识别语种
        :param engineType: 普通话(sms16k, sms8k)，英语(sms-en8k, sms-en16k)
        :return: Success or Fail
        """
        if isinstance(engineType, str):
            self._ISRParams['engine_type'] = engineType
            return True
        else:
            print("Engine Type int ISR has a wrong type: ", type(engineType))
            return False

    @property
    def Params(self):
        res = ["%s:%s" % ('\"'+key+'\"', '\"'+value+'\"') for key, value in self._ISRParams.items()]
        res = ','.join(res)
        res = '{' + res + '}'
        print(res)
        return res

    @Params.setter
    def Params(self, value):
        if isinstance(value, str):
            values = value.split(',')
            for kv in values:
                kvs = kv.split(':', 2)
                if len(kvs) == 2:
                    self._ISRParams[kvs[0].strip()] = kvs[1].strip()
        elif isinstance(value, dict):
            self._ISRParams.update(value)


if __name__ == '__main__':
    param = ISRParams()
    print(param.Params)

    testP = "aue:raw, engine_type:sms-en16k"
    param.Params = testP
    print(param.Params)
