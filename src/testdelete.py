import os
import glob
files = glob.glob('C:/Users/vibho/Desktop/"Test Me"/*')
for f in files:
    os.remove(f)