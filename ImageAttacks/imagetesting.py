import os
from results import *

# Get all images from the ./images/ directory
from os import listdir
from os.path import isfile, join
files = [f for f in listdir("./images/") if isfile(join("./images/", f))]

os.system("cp results.py backup.py")	# Create a backup, just in case

for f in files:
   s=f.split('-')
   idx=s[0]
   os.system("vlc -fL ./images/"+f)
   succ = raw_input("Enter number of successes (out of 5): ")
   try:
      result[idx]+=int(succ)
   except KeyError:
      result[idx]=0

file = open("results.py","w")
file.write("result="+str(result))
file.close()

