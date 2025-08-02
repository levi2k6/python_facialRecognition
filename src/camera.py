import cv2 
import time

import faceAngleChecker 

capture = cv2.VideoCapture(0)

captured = False

credentialFace = None 

def cameraCapture():

    global captured
    global credentialFace

    if not capture.isOpened():
        print ("Error: Cannot access the camera")
        exit()

    while True:
        ret, frame = capture.read()

        if not ret:
            print("Failed to grab frame.")
            break

        rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        faceAngle = faceAngleChecker.checkFaceAngle( rgbImage, frame)

        if faceAngle:

            threshold = faceAngleChecker.THRESHOLD 

            if abs(faceAngle.pitch) < threshold and abs(faceAngle.yaw) < threshold and not captured:
                timestamp = int(time.time())
                filename = f"capture_{timestamp}.jpg"
                cv2.imwrite(f"../assets/{filename}", frame)
                print(f"Captured photo: {filename}")
                captured = True
            else:
                print("Angle not valid");

        else:
            captured = False

        cv2.imshow("Webcam", frame)

        if ( cv2.waitKey(1) & 0xFF == ord("q") ) or captured == True:
            credentialFace = frame;
            break
    capture.release()
    cv2.destroyAllWindows()
    return credentialFace;

