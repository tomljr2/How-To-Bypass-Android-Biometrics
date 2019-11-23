import cv2

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cam.set(3,1920)
cam.set(4,1080)
i = 0
while True:
   ret_val, img = cam.read()
   img = cv2.flip(img, 1)
   if i < 10:
      cv2.putText(img, "Take close picture. Press q when done.", \
                  (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0))
   elif i < 20:
      cv2.putText(img, "Take medium picture. Press q when done.", \
                  (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0))
   elif i < 30:
      cv2.putText(img, "Take far picture. Press q when done.", \
                  (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0))

   cv2.imshow('Biometrics Testing Recording', img)
   if cv2.waitKey(1) == ord('q'):
       if i < 10:
           cv2.imwrite("./images/close-"+str(i)+".png",img)
       elif i < 20:
           cv2.imwrite("./images/med-"+str(i-10)+".png",img)
       elif i < 30:
           cv2.imwrite("./images/far-"+str(i-20)+".png",img)
       i+=1
       if i==30:
          break
cv2.destroyAllWindows()

