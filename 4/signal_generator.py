import r2r_dac as r2r
import time
import matplotlib.pyplot as plt
import numpy as np

ampl = 3.2
sign_f = 10
samp_f = 1000
v =  []
t = []

def get_sin(freq, time):
    return (numpy.sin(2*numpy.pi*freq*time)+1)/2

def wait(s_f):
    time.sleep(1/s_f)


try:
    dac = r2r.R2R_DAC([16,20,21,25,26,17,27,22], 3.183, True)
    start_time = time.time()
    while true:
        c_t = t.time() - start_t
        t.append(c_t)
        s = ampl*sg.get_sin(sign_f, c_t)
        v.append(s)
        sg.wait(s_f)
finally:
    dac.deinit()
    t1 = np.arrange(0, max(t), 1/s_f)
    sawtooth = (ampl * 2* s_f*t)%(2**ampl)
    triangle = ampl - np.abs(sawtooth - ampl)
    plt.plot(t, triangle)
    plt.grid()
    plt.show()