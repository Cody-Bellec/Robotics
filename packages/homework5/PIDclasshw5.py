#!/usr/bin/env python3

import time
from std_msgs.msg import Float32

class PID:
    def __init__(self, firstError):
        self.KP = 0.15
        self.KI = 0.01
        self.KD = 0.4
        t1 = t.time()
        self.laterError = firstError
        
    def changeGainz(self, KPc, KIc, KDc):
        self.KP = KPc
        self.KI = KIc
        self.KD = KDc
    
    def calc(self, error):
        alphaT = t.time()-T1
        
        self.signal = (self.KP*error) + (self.KI * alphaT) + (self.KD *((error-self.laterError)/alphaT))
        self.laterError = error
        
        return self.signal
    
