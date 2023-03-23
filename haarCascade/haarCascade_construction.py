import cv2

vid = cv2.VideoCapture("C:\PycharmProjects\Opencv\Arac_algilama\(v)ideoda_arac_algilama.mp4")
car_cascade = cv2.CascadeClassifier("C:\PycharmProjects\Opencv\haarCascade_yapimi\car_cascade.xml")

while 1:
    ret, frame = vid.read()
    frame = cv2.resize(frame, (640, 360))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.3, 3)

    for (x, w, y, h) in cars:
        cv2.rectangle(frame, (x, y), (x + y, x + h), (255, 0, 0), 3)
        # this inside (x + y, x + h) part depends on how you want to draw the rectangle for the rectangle in the video

    cv2.imshow("video", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows().CascadeClassifier()