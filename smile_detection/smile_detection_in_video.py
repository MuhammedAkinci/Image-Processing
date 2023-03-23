import cv2

vid = cv2.VideoCapture("C:\PycharmProjects\Opencv\gulumseme_algilama\(v)ideoda_gulumseme_algilama.mp4")

smile_cascade = cv2.CascadeClassifier('C:\PycharmProjects\Opencv\gulumseme_algilama\(r)esimde_gulumseme_algilama.xml')
face_cascade = cv2.CascadeClassifier('C:\PycharmProjects\Opencv\yuz_algilama\(y)uz_algilama1.xml')

while 1:
    ret, frame = vid.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.4, 9)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        roi_frame = frame[y:y+h, x:x+w]
        roi_gray = gray[y:y+h, x:x+w]

        smiles = smile_cascade.detectMultiScale(roi_gray, 1.2,2)

        for (sx, sw, sy, sh) in smiles:
            cv2.rectangle(roi_frame, (sx,sy), (sx+sw,sy+sh),(0,255,0),2)


    cv2.imshow('videos', frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()