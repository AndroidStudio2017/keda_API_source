"""
EMR情感识别参数类，封装一些EMR需要的参数，有待后续扩展...
"""


class EMRParam:
    """
    EMR情感识别参数类
    """

    def __init__(self):
        """
        初始化EMR参数
        """
        self.resource = './resouce'
        self.audio = ''
        self.tab = ['', 'ANGRY', 'FEAR', 'HAPPY', 'NEUTRAL', 'SAD']
        # 可能会有一些训练参数

    @property
    def resourceDir(self):
        """
        resourceDir的get方法
        :return: 资源文件路径
        """
        assert self.resource is not None
        return self.resource

    @resourceDir.setter
    def resourceDir(self, value):
        """
        resourceDir的set方法
        :param value: 设置resourceDir
        :return: None
        """
        if isinstance(value, str):
            self.resource = value
        else:
            print('EMR Param Type Error! resourceDir(Not String) ', value, '==>', type(value))

    @property
    def table(self):
        """
        table的get方法
        :return: 情感识别范围的list
        """
        assert self.tab is not None
        return self.tab

    @table.setter
    def table(self, value):
        """
        table的set方法
        :param value: 用户需要设置的情感识别范围list
        :return: None
        """
        if isinstance(value, list):
            self.tab = value
        else:
            print('EMR Param Type Error! table(Not List) ', value, '==>', type(value))

    @property
    def audioPath(self):
        """
        audioPath的get方法
        :return: 待识别音频路径
        """
        assert self.audio is not None
        return self.audio.encode()

    @audioPath.setter
    def audioPath(self, value):
        """
        audioPath的set方法
        :return: None
        """
        if isinstance(value, str):
            self.audio = value
        else:
            print('EMR Param Type Error! audioPath(Not string) ', value, '==>', type(value))

