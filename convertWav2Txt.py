# Written by Sylvester Benson-Sesay
# sbensons@u.rochester.edu
# Generates text data from .wav files

from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

_array = np.empty((132300), float) # create an empty array (initializatio)
for j in range (1,3):
    fs, data = wavfile.read('/Users/sylvesterbenson-sesay/Desktop/Siren-44100-16bit-mono/CarBackground{0}.wav'.format(j))
    i = 0 # initailize i afteer each j loop
    numchunk = (len(data))//(3*fs) # number of iterations
    for i in range(1,numchunk+1):
        _chunk = data[(i-1)*3*fs:3*i*fs] #moving chunk
        _max = (np.amax(_array)) # max to normalize
        _chunk = _chunk/_max # normalize from 0 to 1

        sos = signal.butter(5, 100, 'highpass', fs=fs, output='sos') # pass it through a high pass filter
        audio = signal.sosfilt(sos, _chunk)

        sos = signal.butter(5, 3000, 'lowpass', fs=fs, output='sos') # pass it through a low pass filter
        _chunk = signal.sosfilt(sos, audio)

        _array = np.vstack((_array,_chunk)) # preprocessed data.
        i+=1
        print(_array.shape)
        
