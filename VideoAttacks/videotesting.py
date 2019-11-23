from config import *
from results import *
import os
import time

# Get all videos in the ./videos/ directory
from os import listdir
from os.path import isfile, join
files = [f for f in listdir("./videos/") if isfile(join("./videos/", f))]

os.system("cp results.py backup.py")	# Create a backup, just in case

for rate in rates:
   os.system("xrandr --output " + monitor + " --mode " + resolution +	\
             " -r " + rate)
   for f in files:
      s=f.split("-")
      idx=s[0]+"-"+s[2]+"-"+rate
      os.system("vlc -fL ./videos/"+f)
      succ = raw_input("Enter number of successes (out of 5): ")
      try:
         result[idx]+=succ
      except KeyError:
         result[idx]=0

file = open("results.py","w")
file.write("result="+str(result))
file.close()

# Reset to what I use
os.system("xrandr --output DP-4 --mode 2560x1440 -r 144")
# Empty the contents of the videos directory
os.system("rm ./videos/*")
