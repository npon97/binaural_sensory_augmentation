import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile 
from scipy.signal import firwin

HRTF_L_path = (
  "/home/phippsy/masters-proj/full/elev-10/L-10e090a.dat"
)
HRTF_R_path = (
  "/home/phippsy/masters-proj/full/elev-10/R-10e090a.dat"
)

FUNK_PATH = "/home/phippsy/masters-proj/funky.wav"
OUTPUT_AUDIO_PATH = "/home/phippsy/masters-proj/funky_3d.wav"

title_l = HRTF_L_path.split("/")[-1]
title_r = HRTF_R_path.split("/")[-1]


# i is signed integer
# u is unsigned integer
# > is big endian, < is little endian
# The number after specifies the number of bytes (e.g. 2 = 2 bytes / 16 bits)
leftHRTF = np.fromfile(HRTF_L_path, dtype='>i2') # big-endian signed 16 bit integer
rightHRTF = np.fromfile(HRTF_R_path, dtype='>i2')# big-endian signed 16 bit integer

leftimp = np.fft.ifft(leftHRTF) # obtain the inverse fourier transform
rightimp = np.fft.ifft(rightHRTF) # of the transfer function

size_taps_l = len(leftimp)
size_taps_l = len(rightimp)

# Plot the raw values from the HRTF files
# plt.figure(figsize=(10,15))
# plt.subplot(2, 1, 1)
# plt.plot(leftimp, 'bo-')
# plt.title(title_l)
# plt.xlabel(f"Taps / Coefficients (N={size_taps_l})")

# plt.subplot(2, 1, 2)
# plt.plot(rightimp, 'ro-')
# plt.title(title_r)
# plt.xlabel(f"Taps / Coefficients (N={size_taps_l})")
# plt.show()

fs, sound_in = wavfile.read(FUNK_PATH) # Read the audio data
# left_channel = sound_in[0:]
# right_channel = sound_in[1:]

left_channel, right_channel = np.hsplit(sound_in, 2)

# The [0] removes the outer list
left_channel = np.reshape(left_channel, (1, -1))[0] 
right_channel = np.reshape(right_channel, (1, -1))[0]

print(left_channel.shape)
print(leftimp.shape)


'''
# taps = 512
# sound samples = 846720
'''

# Convolve the values with an input signal 
spatial_l = np.convolve(left_channel, leftimp, mode='valid')
spatial_r = np.convolve(right_channel, rightimp, mode='valid')


print(spatial_l.shape)
print(spatial_r.shape)

spatial_out = np.hstack((spatial_l, spatial_r))

wavfile.write(OUTPUT_AUDIO_PATH, fs, spatial_out)
