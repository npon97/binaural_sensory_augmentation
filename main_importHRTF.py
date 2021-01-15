import numpy as np

HRTF_path = (
  "/home/phippsy/Documents/BinauralMastersProject/compact/elev-10/H-10e090a.dat"
)

# i is signed integer
# u is unsigned integer
# > is big endian, < is little endian
# The number after specifies the number of bytes (e.g. 2 = 2 bytes / 16 bits)
data = np.fromfile(HRTF_path, dtype='>i2') # big-endian signed 16 bit integer 

leftimp = data[0:256:2]
rightimp = data[1:256:2]

print(leftimp)
print(rightimp)
