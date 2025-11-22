import cv2
import numpy as np
from mss import mss
from config import JPEG_QUALITY


class ScreenCapturer:
    def __init__(self, monitor_idx=1):
        self.sct = mss()
        try:
            self.monitor = self.sct.monitors[monitor_idx]
        except IndexError:
            print("Monitor was not found, using main.")
            self.monitor = self.sct.monitors[1]

    def get_frame_bytes(self):
        img = self.sct.grab(self.monitor)
        frame = np.array(img)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)


        _, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), JPEG_QUALITY])

        return buffer.tobytes()