import numpy as np
import matplotlib.pyplot as plt

HRTF_L_path = (
  "/home/phippsy/masters-proj/full/elev-10/L-10e090a.dat"
)
HRTF_R_path = (
  "/home/phippsy/masters-proj/full/elev-10/R-10e090a.dat"
)

# i is signed integer
# u is unsigned integer
# > is big endian, < is little endian
# The number after specifies the number of bytes (e.g. 2 = 2 bytes / 16 bits)
leftimp = np.fromfile(HRTF_L_path, dtype='>i2') # big-endian signed 16 bit integer 
rightimp = np.fromfile(HRTF_L_path, dtype='>i2') #big-endian signed 16 bit integer 

print(leftimp)
print(rightimp)

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(leftimp)

plt.subplot(2, 1, 2)
plt.plot(rightimp)


plt.show()