# Binaural Masters Project <Insert Better Title>
  
This project will attempt some spatialization of sound and how it affects a  
human's sense of direction

---
## Viewing some open source HRTFs in the KEMAR data set with Python
Here are some steps to follow to reproduce the viewing of the HRTF values  
from the KEMAR data set.
* Go to `https://sound.media.mit.edu/resources/KEMAR/` and 
download `compact.tar.Z`.
* Unzip the downloaded folder
* Go to a unix prompt and use `od` to view the HRTF values of one of the files, 
lets say `elev-10/H-10e100a.dat`. Because this is in a binary format, it is 
important to run `od` with *big-endian* and *signed-16bit (2-byte)* options. 
This is done with the following command:  
`od H-10e100a.dat --endian=big --format=d2 -w8`  
  
This option should output something like:  
```
0000000      1    190      0   -330
0000010      0    387      0   1066
0000020      1  17124      1  -1610
0000030      1 -30496      1   1111
0000040      0  14949      1   2911
0000050      . . .
.
.
.
```
  
It can be seen at line 3 that the maximum value `-30296` exists, which happens  
to be the maximum value of the compact data.