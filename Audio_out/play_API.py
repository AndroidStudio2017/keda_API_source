"""

定义了音频输出有关接口API    play
                          show_out_devices

"""
import os


def play(pp):
    """
    调用shell参数进行播音，相应参数在PlayParam中
    :param pp: PlayParam类
    :return: None
    """
    os.system(pp.params)


def show_out_device():
    """
    查看所有音频输出设备
    :return: None
    """
    os.system('aplay -l')
