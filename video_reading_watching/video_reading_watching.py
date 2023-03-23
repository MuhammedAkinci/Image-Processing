import cv2

''''
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) # this flip function allows us to reflect the image we receive according to the axis we want, when we set it to 0, for example, we get it reversed
    cv2.imshow("Webcam", frame)
    #cv2.waitKey(30)

    if cv2.waitKey(1) & 0xFF == ord("q"): # the purpose of this is to close it the way we want, so if we say q it closes
        break

cap.release() # our purpose of using this prevents us from getting a different error while currently opening a file
cv2.destroyAllWindows()

'''
'''
# this is what we do below, reading data from an mp4 file installed on our computer and watching the video
cap = cv2.VideoCapture("1.mp4")

while True:
    ret, frame = cap.read()

    if ret == 0: # this is for the video to close by itself when the playing time is over and exit the endless loop
        break
    frame = cv2.flip(frame, 1) # this flip function allows us to reflect the image we receive according to the axis we want, when we set it to 0, for example, we get it reversed
    cv2.imshow("1", frame)
    #cv2.waitKey(30)

    if cv2.waitKey(30) & 0xFF == ord("q"):#the purpose of this is to close it the way we want, so if we say q, it closes
        break

cap.release() # our purpose of using this prevents us from getting a different error while currently opening a file
cv2.destroyAllWindows()
'''