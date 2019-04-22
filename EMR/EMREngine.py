
from src.EMR.EMR_API import *


class EMREngine:
    """
    EMREngine类，用于实现EMR
    """
    def __init__(self):
        self._is_error = False
        self._is_running = False

        self.resource = './resource'
        self.audioPath = './audio/test.wav'
        self.tab = ['', 'ANGRY', 'FEAR', 'HAPPY', 'NEUTRAL', 'SAD']

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

    def SetResouce(self, resource):
        if self._is_error or self._is_running:
            return False
        _state = True
        if isinstance(resource, str):
            self.resource = resource
        else:
            self._is_error = True
            _state = False
        return _state

    def run(self):
        if self._is_error or self._is_running:
            return False
        _state = True
        emr = EMR()
        emr.SetAudioPath(self.audioPath)
        emr.SetResourceDir(self.resource)
        res_id, res_text = emotion_recognition(emr)
        print(res_id, ":", res_text)
