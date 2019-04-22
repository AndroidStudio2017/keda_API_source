"""

定义了 ISRSessionParam类, 封装了语音合成会话参数

"""
from collections import OrderedDict


class ISRSessionParam:
    """
    语音识别参数类
    """
    def __init__(self):
        """
        初始化默认参数
        """
        self._session_begin_params = OrderedDict()
        self._session_begin_params['sub'] = 'iat'
        self._session_begin_params['domain'] = 'iat'
        self._session_begin_params['language'] = 'zh_cn'
        self._session_begin_params['accent'] = 'mandarin'
        self._session_begin_params['sample_rate'] = '16000'
        self._session_begin_params['result_type'] = 'plain'
        self._session_begin_params['result_encoding'] = 'utf8'



    @property
    def params(self):
        """
        合成传给讯飞的参数
        :return: 用,分割参数的字符串
        """
        results = ['%s = %s' % (key, value) for key, value in self._session_begin_params.items()]
        return ','.join(results)

    @params.setter
    def params(self, value):
        """
        设置参数值
        :param value: 设置参数值(接受字符串和字典)
        :return: None
        """
        if isinstance(value, str):
            values = value.split(',')
            for kv in value:
                kvs = kv.split('=', 2)
                if len(kvs) == 2:
                    self._session_begin_params[kvs[0].strip()] = kvs[1].strip()
        elif isinstance(value, dict):
            self._session_begin_params.update(value)
