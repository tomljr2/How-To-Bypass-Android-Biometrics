# Bypassing Android Biometrics Research

The purpose of this research is to understand how an attacker could easily
bypass Android biometrics. I go into this by making the assumptions that the
victim used Android biometrics to authenticate themself into their device and
that the attacker is not an technological expert and that they have access
to images / videos of the victim (most likely through social media).

Since the attacker cannot be an expert, the attacks must be simple enough
for anyone to easily perform the attack only with common household items.
The goal of this research is to analyse which simple attacks are the most
effective, and in turn this will see which biometrics are most prone to
being compromised. In knowing this, it gives a baseline to researchers
for what biometrics future research should be most focused on. 

## Types of Biometrics

There are four main types of Android biometrics. Iris recognition, face
recognition, fingerprint scanning, and voice recognition. Voice recognition
was deprecated in Android 8.0, so this research does not focus on that.

## Video Attacks

Video attacks are used for iris and face recognition as an attempted method
of bypassing them by simply replaying a video of the victim. The code
provided gives a method to test in a variety of settings including different
resolutions, distances, and monitor refresh rates.

### Preparing to test video attacks

To begin, you will need to install the necessary dependencies, if you do not
already have them.


```
   pip install datetime opencv-python
```

You will also need to install xrandr and vlc onto your system if you do not
already have it.

Within the VideoAttacks folder, there exists a config.py file. This will need
to be adjusted for your system. To get the necessary information, you will need
to start by typing the command:


```
xrandr
```

This will give a list of monitors that are connected to your computer and the
resolution / refresh rates that is supported by that monitor. Find the name of
your monitor (It should be something like "HDMI-0" or "DP-4"). Find the supported
refresh rates that you would like to test at (in my case 50Hz, 60Hz, and 100Hz
[these were chosen because it is likely closest to the shutter speed of the camera]).

Using the values you have obtained, replace the values in config.py with the ones
you have. I recommend keeping the resolution at 1920x1080 even if you have a higher
resolution monitor. I do not recommend using a monitor with a lower resolution than
1920x1080.

For the values of defaultRes and defaultRate, simply use the resolution and refresh
rate that you normally use. This just makes sure that your computer is set back to
how it was prior to testing.

Now you can run:

```
python videocapturing.py
```

Your default webcam (this MUST support 1080px30fps, 720px60fps, 480px60fps, otherwise
it will scale the video down) will begin recording and it will say how close to keep
your face and then press q when done. It will then record a video and repeat the process
at a new distance. After this is done three times, it will do it all again at a different
resolution with three different resolutions, resulting in nine total videos.

Once you have completed this, check the length of the videos. They should be approximately
10 seconds. If they are not, then you will need to tweak the values of cfps1, cfps2, and
cfps3 in config.py. These are dependent on the number of threads supported by your computer,
so it likely will not be the same values as mine.

### Testing video attacks

Once everything has been set up, you can record the videos once again by using:

```
python videocapturing.py
```

and following the same method as before. This should be done once for every subject that is
being tested. Once all of the videos have been created, you can then run:

```
python videotesting.py
```

This will replay the videos in a loop at different refresh rates. This can be a long and
tedious process, so be prepared. When a video comes up, you will attempt to bypass the
biometric five times (your device will temporarily no longer allow you to use biometrics to
unlock the device at this point, that is how you know when to move on). Once this is
completed, simply close vlc and when it prompts to enter the number of successes, simply
put in the number of times your device was unlocked. This will be stored in results.py
after you have completed all 27 trials and if anything goes wrong in the process,
results.py is saved in backup.py when starting videotesting.py. All videos will be deleted
once you have completed the process, and you can begin again. Keep note of the total number
of trials though because results.py will only track number of successes. 

## Image attacks

Image attacks are just a simpler case of video attacks. They are also used with iris recognition
and face recognition. The testing done looks at images taken at different distances and various
refresh rates.


### Preparing to test image attacks

To begin, you will need to install the necessary dependencies, if you do not
already have them.


```
   pip install opencv-python
```

You will also need to install vlc onto your system if you do not already have it.

Within the ImageAttacks folder, there exists a config.py file. This will need
to be adjusted for your system. To get the necessary information, you will need
to start by typing the command:

This will give a list of monitors that are connected to your computer and the
resolution / refresh rates that is supported by that monitor. Find the name of
your monitor (It should be something like "HDMI-0" or "DP-4"). Find the supported
refresh rates that you would like to test at (in my case 50Hz, 60Hz, and 100Hz
[these were chosen because it is likely closest to the shutter speed of the camera]).

Using the values you have obtained, replace the values in config.py with the ones
you have. I recommend keeping the resolution at 1920x1080 even if you have a higher
resolution monitor. I do not recommend using a monitor with a lower resolution than
1920x1080.

For the values of defaultRes and defaultRate, simply use the resolution and refresh
rate that you normally use. This just makes sure that your computer is set back to
how it was prior to testing.

### Testing image attacks

Once everything has been set up, you can record the videos once again by using:

```
python imagecapturing.py
```

Your default webcam (which MUST support 1080p 30fps or it will be scaled down) will
start recording. A distance for you to take the picture from will be shown on the
video and you will press q to take a picture. Take ten pictures and repeat at the
new distance. This will be done three times for a total of 30 pictures. These will
be saved in the ./images/ directory.

Once completed, you can run:

```
python imagetesting.py
```

This will show an image in vlc at a specfic refresh rate and you will test it five 
times. Once completed, close vlc and input the number of successes out of the five 
attempts. Repeat this process until no more images are shown. There should be 90
images in total shown per subject. The results will be stored in results.py and
a backup will be made in backup.py each time imagetesting.py is started, just in
case of any mistakes. Keep track of the total number of tests in each category on
your own, because results.py only tracks successes.  
