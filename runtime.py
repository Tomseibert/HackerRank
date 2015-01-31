__author__ = 'MonkeyBoy'

import time

class Runtime:
    version = "0.4"
    # class to help track run times
    def __init__(self,sTime =0):
        self.startTime = sTime
        self.laps = []

    def start(self):
        self.startTime = time.time()

    def lap(self):
        self.laps.append(time.time())
        return self.laps[-1] - self.startTime
