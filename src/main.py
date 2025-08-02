import faceRecognition;
import camera;

image1 = "../assets/ryan_gosling.jpg";
image2 = "../assets/forsen_crossArm.webp";

def main():

    credentialFace = camera.cameraCapture();
    faceRecognition.authenticateFace(credentialFace);

main();



