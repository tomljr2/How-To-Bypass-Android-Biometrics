from config import *
import os
import time

for rate in rates:
   os.system("xrandr --output " + monitor + " --mode " + resolution +	\
             " -r " + rate)
   os.system("xrandr")
   time.sleep(5)
