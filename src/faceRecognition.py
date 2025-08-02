import face_recognition
import cv2 

reference1 = "../assets/reference2.jpg";
reference2 = "../assets/capture_1754057623.jpg";

def authenticateFace( credentialFace ):

    # rgb_credentialFace = cv2.cvtColor(credentialFace, cv2.COLOR_BGR2RGB)
    #
    # face1_encodings = face_recognition.face_encodings(rgb_credentialFace)
    # if len(face1_encodings) == 0:
    #     print("❌ No face found in the credential image.")
    #     return

    print("credentialFace: ", credentialFace);

    face1 = face_recognition.load_image_file(reference1); 
    face1_encoding = face_recognition.face_encodings(face1)[0];
    face2 = face_recognition.load_image_file(reference2); 
    face2_encoding = face_recognition.face_encodings(face2)[0];

    results = face_recognition.compare_faces([face1_encoding], face2_encoding);
    face_distance = face_recognition.face_distance([face1_encoding], face2_encoding);

    if results[0]:
        print("face matched");
    else:
        print("face does not match");

    print("face distance: ", face_distance[0]);
