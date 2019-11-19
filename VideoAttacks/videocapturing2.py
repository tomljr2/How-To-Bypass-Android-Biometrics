import datetime
from threading import Thread
import cv2
from cfpsList import *

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

class recordVideo:
   def __init__(self,height,width,fps,fourcc,output,overlay):
      self.height=height
      self.width=width
      self.fps=fps
      self.cfps=cfpsList[(height,width,fps)]
      self.fourcc=fourcc
      self.output=output
      self.overlay=overlay
   def setOverlay(self,overlay):
      self.overlay=overlay
   def display(self):
      cam = WebcamVideoStream(self.fourcc,self.cfps,self.height,self.width).start()
      while True:
         frame = cam.read()
         cv2.putText(frame, self.overlay+" Press q when done.", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0))
         cv2.imshow("Adjust face",frame)
         key = cv2.waitKey(int(1000/self.cfps)) & 0xFF
         if key == ord('q'):
            break;
      cam.stop()
      cv2.destroyAllWindows()
   def record(self):
      cam = WebcamVideoStream(self.fourcc,self.cfps,self.height,self.width).start()
      rec = cv2.VideoWriter(self.output,self.fourcc,self.fps,(self.height,self.width))
      start = datetime.datetime.now()
      while True:
         frame = cam.read()
         rec.write(frame)
         cv2.imshow("Recording...",frame)
         key = cv2.waitKey(int(1000/self.cfps)) & 0xFF
         if (datetime.datetime.now() - start).total_seconds() > 10:
            rec.release()
            break;
      cam.stop()
      cv2.destroyAllWindows()

h=1920
w=1080
f=30
fourcc=cv2.VideoWriter_fourcc(*'MJPG')

record = recordVideo(h,w,f,fourcc,"test.avi","Put face 10cm from camera.")
record.display()
record.record()
