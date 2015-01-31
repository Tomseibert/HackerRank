__author__ = 'MonkeyBoy'

import time

class Runtime:
    version = "0.1"
    # class to help track run times
    def __init__(self,sTime =0):
        self.startTime = sTime
        self.laps = []

    def start(self):
        self.startTime = time.clock()

    def lap(self):
        self.laps.append(time.clock())
        return self.laps.pop() - self.startTime

    def ver(self):
        return version
