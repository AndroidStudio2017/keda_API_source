import ctypes
import wave
import numpy as np
import scipy.signal as sps


def load_dll_msc(dllpath):
    """
    加载动态链接库
    :param dllpath: dll路径
    :return: dll
    """
    obj = ctypes.cdll.LoadLibrary(dllpath)
    return obj


def get_c_char_p(src_text):
    """
    将 src_text 转换为 c_char_p 类型, 用于传入讯飞的参数
    :param src_text: 待转换字符串
    :return: c_char_p类型字符串
    """
    if src_text is None:
        c_text = ctypes.POINTER(ctypes.c_char)()
    elif isinstance(src_text, str):
        c_text = ctypes.c_char_p(src_text.encode('utf-8'))
    else:
        print(type(src_text))
        c_text = src_text

    return c_text


def write_binary_file(path, content):
    """
    将二进制文件流content写入path路径中
    :param path: 存储文件路径
    :param content: 二进制文件内容
    :return: None
    """
    with open(path, 'wb') as fp:
        fp.write(content)
    fp.close()


class DownSample:
    def __init__(self):
        self.in_rate = 16000.0
        self.out_rate = 8000.0

    def open_file(self, fname):
        try:
            self.in_wav = wave.open(fname)
        except:
            print("Cannot open wav file (%s)" % fname)
            return False

        if self.in_wav.getframerate() != self.in_rate:
            print("Frame rate is not %d (it's %d)" % \
                  (self.in_rate, self.in_wav.getframerate()))
            return False

        self.in_nframes = self.in_wav.getnframes()
        print("Frames: %d" % self.in_wav.getnframes())

        if self.in_wav.getsampwidth() == 1:
            self.nptype = np.uint8
        elif self.in_wav.getsampwidth() == 2:
            self.nptype = np.uint16

        return True

    def resample(self, fname):
        self.out_wav = wave.open(fname, "w")
        self.out_wav.setframerate(self.out_rate)
        self.out_wav.setnchannels(self.in_wav.getnchannels())
        self.out_wav.setsampwidth (self.in_wav.getsampwidth())
        self.out_wav.setnframes(1)

        print("Nr output channels: %d" % self.out_wav.getnchannels())

        audio = self.in_wav.readframes(self.in_nframes)
        nroutsamples = round(len(audio) * self.out_rate/self.in_rate)
        print("Nr output samples: %d" %  nroutsamples)

        audio_out = sps.resample(np.fromstring(audio, self.nptype), nroutsamples)
        audio_out = audio_out.astype(self.nptype)

        self.out_wav.writeframes(audio_out.copy(order='C'))

        self.out_wav.close()
