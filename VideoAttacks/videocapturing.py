import datetime
from threading import Thread
import cv2
from config import *
import os

# This is a class to handle the recording using multiple threads.
# Because the recorded framerate and captured framerate do not
# sync up, I created cfps (compensation fps) to record at a high
# framerate which will be captured at a lower framerate (the actual
# framerate) so that the output video plays correctly. Cfps may
# depend on the number of threads a computer has, so I may make a
# utility to automatically generate cfpsList.py if I have time.
class WebcamVideoStream:
   def __init__(self, fourcc, fps, h, w):
      self.stream = cv2.VideoCapture(0)
      (self.grabbed, self.frame) = self.stream.read()
      self.stopped = False
      self.stream.set(cv2.CAP_PROP_FOURCC, fourcc)
      self.stream.set(cv2.CAP_PROP_FPS, fps)
      self.stream.set(3,h)
      self.stream.set(4,w)
   def start(self):
      Thread(target=self.update, args=()).start()
      return self
   def update(self):
      while True:
         if self.stopped:
            return
         (self.grabbed, self.frame) = self.stream.read()
   def read(self):
      return self.frame
   def stop(self):
      self.stopped = True

# This is a class that uses the above class to record a specified height, width, fps,
# codec for 10 seconds 3 times.
class recordVideo:
   def __init__(self,height,width,fps,fourcc,output,overlay):
      self.height=height
      self.width=width
      self.fps=fps
      self.cfps=cfpsList[(height,width,fps)]
      self.fourcc=fourcc
      self.output=output
      self.overlay=overlay
   def record(self):
      cam = WebcamVideoStream(self.fourcc,self.cfps,self.height,self.width).start()
      recording=False
      init = True
      numRecs=0
      while numRecs!=1:
         if recording and init:
            rec = cv2.VideoWriter(self.output+str(numRecs)+".avi",self.fourcc,self.fps,(self.height,self.width))
            init = False
         frame = cam.read()
         cv2.imshow("Biometrics Testing Recording",frame)
         if not recording:
            cv2.putText(frame, self.overlay+" Press q when done.", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0))
         else:
            cv2.putText(frame, str(numRecs), (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (0, 255, 0))
            rec.write(frame)
            if (datetime.datetime.now() - start).total_seconds() >= 10:
               rec.release()
               init=True
               numRecs+=1
               start=datetime.datetime.now()
         key = cv2.waitKey(int(1000/self.cfps)) & 0xFF
         if key == ord('q') and not recording:
            recording=True
            start=datetime.datetime.now()
      cam.stop()
      cv2.destroyAllWindows()

# These consist of 1.5 minutes of recordings saved in ./videos/

# TEST RECORD AT 1920x1080x30fps

h=1920
w=1080
f=30
fourcc=cv2.VideoWriter_fourcc(*'MJPG')

record = recordVideo(h,w,f,fourcc,"./videos/close-"+str(h)+"-"+str(w)+"-"+str(f)+"-","Put face 10in from camera.")
record.record()
record = recordVideo(h,w,f,fourcc,"./videos/med-"+str(h)+"-"+str(w)+"-"+str(f)+"-","Put face 20in from camera.")
record.record()
record = recordVideo(h,w,f,fourcc,"./videos/far-"+str(h)+"-"+str(w)+"-"+str(f)+"-","Put face 30in from camera.")
record.record()

# TEST RECORD AT 1280x720x60fps

h=1280
w=720
f=60

record = recordVideo(h,w,f,fourcc,"./videos/close-"+str(h)+"-"+str(w)+"-"+str(f)+"-","Put face 10in from camera.")
record.record()
record = recordVideo(h,w,f,fourcc,"./videos/med-"+str(h)+"-"+str(w)+"-"+str(f)+"-","Put face 20in from camera.")
record.record()
record = recordVideo(h,w,f,fourcc,"./videos/far-"+str(h)+"-"+str(w)+"-"+str(f)+"-","Put face 30in from camera.")
record.record()

# TEST RECORD AT 640x480x60fps

h=640
w=480
f=60

record = recordVideo(h,w,f,fourcc,"./videos/close-"+str(h)+"-"+str(w)+"-"+str(f)+"-","Put face 10in from camera.")
record.record()
record = recordVideo(h,w,f,fourcc,"./videos/med-"+str(h)+"-"+str(w)+"-"+str(f)+"-","Put face 20in from camera.")
record.record()
record = recordVideo(h,w,f,fourcc,"./videos/far-"+str(h)+"-"+str(w)+"-"+str(f)+"-","Put face 30in from camera.")
record.record()

