import cv2

img = cv2.imread('C:\PycharmProjects\Opencv\gulumseme_algilama\(r)esimde_gulumseme_algilama.jpg')
smile_cascade = cv2.CascadeClassifier('C:\PycharmProjects\Opencv\gulumseme_algilama\(r)esimde_gulumseme_algilama.xml')
face_cascade = cv2.CascadeClassifier('C:\PycharmProjects\Opencv\yuz_algilama\(y)uz_algilama1.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.3,5)
# we put the coordinates in faces because we can find the smile by looking at the face coordinates

for (x,y,w,h) in faces:

    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    roi_gray = gray[x:x+w,y:y+h]
    # we did it because we will find smiles that are in gray tones
    roi_img = img[x:x+w,y:y+h]
    # represents the area where the face is located, we assigned the places from y to y+h ie downwards and from x to x+h ie to the right to roi_img
    
    smiles = smile_cascade.detectMultiScale(roi_gray,1.3,5)
    for (sx,sy,sw,sh) in smiles:
        cv2.rectangle(roi_img,(sx,sy),(sx+sw,sy+sh),(0,255,0),2)

    cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()