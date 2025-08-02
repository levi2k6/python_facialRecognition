import mediapipe as mp
import numpy as np
import math
import cv2
import myTypes

mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(static_image_mode=False, refine_landmarks=True)

LANDMARK_IDS = [1, 33, 263, 61, 291, 199]

MODEL_POINTS = np.array([
    [0.0, 0.0, 0.0],       
    [-30.0, -125.0, -30.0],
    [30.0, -125.0, -30.0], 
    [-60.0, -70.0, -60.0],
    [60.0, -70.0, -60.0],  
    [0.0, -150.0, -10.0]   
], dtype=np.float32)

THRESHOLD = 10

def getEulersAngles(rvec):
        R, _ = cv2.Rodrigues(rvec)
        sy = math.sqrt(R[0,0]**2 + R[1,0]**2)
        singular = sy < 1e-6

        if not singular:
            x = math.atan2(R[2,1], R[2,2])
            y = math.atan2(-R[2,0], sy)
            z = math.atan2(R[1,0], R[0,0])
        else:
            x = math.atan2(-R[1,2], R[1,1])
            y = math.atan2(-R[2,0], sy)
            z = 0

        return np.degrees([x, y, z])


def checkFaceAngle( rgbImage, frame ):
    results = faceMesh.process(rgbImage)

    if results.multi_face_landmarks:
        h, w, _ = frame.shape

        for faceLandmarks in results.multi_face_landmarks:
            imagePoints = []

            for i in LANDMARK_IDS:
                pt = faceLandmarks.landmark[i]
                x, y = int(pt.x * w), int(pt.y * h)
                imagePoints.append((x,y))
                # cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

            imagePoints = np.array(imagePoints, dtype = np.float32)

            focalLength = w
            center = (w / 2, h / 2)
            cameraMatrix = np.array([
                [focalLength, 0, center[0]],
                [0, focalLength, center[1]],
                [0,0,1]

            ], dtype=np.float32)
            distanceCoefficients = np.zeros((4,1))

            success, rvec, tvec = cv2.solvePnP(MODEL_POINTS, imagePoints, cameraMatrix, distanceCoefficients)

            if success:
                pitch, yaw, roll = getEulersAngles(rvec)
                cv2.putText(frame, f"Pitch: {pitch:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.putText(frame, f"Yaw: {yaw:.2f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.putText(frame, f"Roll: {roll:.2f}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

                return myTypes.FaceAngle(pitch, yaw, roll) 
            else:
                print("solvePnP failed") 
                return False

