import ctypes


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


