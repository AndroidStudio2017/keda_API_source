"""

定义了音频输入有关接口API    record
                          show_in_devices

"""

import os


def record(rp):
    """
    调用shell命令进行录音, 相应参数在recordParam类中
    :param recordParam: recordParam类
    :return: None
    """
    os.system(rp.params)


def show_in_devices():
    """
    查看现有声卡录音设备
    :return: None
    """
    os.system('arecord -l')



