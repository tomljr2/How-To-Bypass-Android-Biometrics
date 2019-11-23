# Config settings that need to be changed for your computer.

# To set, you will need to use xrandr to find the monitor output name,
# (mine is DP-4), your resolution, and all of the available refresh
# rates that your monitor supports.
monitor="DP-4"
resolution="1920x1080"
rates=["50,","60","100"]	# List of tested refresh rates

cfps1=50
cfps2=105
cfps3=75

# Do not change this
cfpsList = {(1920,1080,30):cfps1,(1280,720,60):cfps2,(640,480,60):cfps3}
