import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import numpy as np

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

textList = ["A B C D E F G H I J K L M N O P Q R S T U V W X Y Z "]

sen = 10  # more is less
while True:
    success, img = cap.read()
    imgText = np.zeros_like(img)
    img,faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]

        # for drawing
        # cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)
        # cv2.circle(img,pointLeft,5,(255,0,255),cv2.FILLED)
        # cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
        w, _ = detector.findDistance(pointLeft, pointRight)
        W = 6.3

        # finding the focal length
        # d = 50
        # f = (w*d)/W
        # print(f)

        # finding the distance
        f = 840
        d = (W * f) / w
        # print(d/100)

        cvzone.putTextRect(img, f'Depth: {int(d/100)}',
                           (face[10][0] - 100, face[10][1] - 50),
                           scale=2)
        for i, text in enumerate(textList):
            singleHeight = 20 + int((int(d/sen)*sen)/4)
            scale = 0.4 + (int(d/sen)*sen)/75
            cv2.putText(imgText, text, (50, 50 + (i * singleHeight)),
                        cv2.FONT_ITALIC, scale, (255, 255, 255), 2)
    imgStacked = cvzone.stackImages([img, imgText], 2, 1)

    cv2.imshow("Image", img)
    if cv2.waitKey(1)==ord('q'):
      break
cap.release()
cv2.destroyAllWindows(); 
