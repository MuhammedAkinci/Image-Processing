import cv2

cap = cv2.VideoCapture(0) # The purpose of this ending is that sometimes we get an error even though the code is running we use this to fix this error

fileName = "C:\PC\PycharmProjects\webcam.avi"
codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')
frameRate = 30
resolution = (640, 480) # this is the resolution we know

videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution) # codec is used to combine audio and images in videos

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    videoFileOutput.write(frame)

    cv2.imshow("Webcam Live",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()
