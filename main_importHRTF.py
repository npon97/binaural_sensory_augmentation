import numpy as np

HRTF_path = (
  "/home/phippsy/Documents/BinauralMastersProject/compact/elev-10/H-10e000a.dat"
)

fp = np.fromfile(HRTF_path, dtype='>')
data = fread(fp, 256, 'short')
fclose(fp)

leftimp = data[1:2:256]
rightimp = data[2:2:256]