from src.Audio_out.class_play_param import *
from src.Audio_out.play_API import *


class playEngine:
    """
    playEngine类, 用于播放音乐
    """
    def __init__(self):
        self._is_error = False
        self._is_running = False

        self.audioPath = './audio/test.wav'

    def SetAudioPath(self, audioPath):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(audioPath, str):
            self.audioPath = audioPath
        else:
            self._is_error = True
            _state = False
        return _state

    def run(self):
        pp = PlayParam()
        pp.params = self.audioPath
        play(pp)

