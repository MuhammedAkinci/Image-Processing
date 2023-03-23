import cv2
import numpy as np
import requests

url = "http://192.168.1.40:8080//shot.jpg"

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) # An arrangement of a small array in image_resp.content
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)# allows us to see the image from the operation we have taken from this memory, that is, the operation we have done in the next line
    img = cv2.resize(img, (640,480))

    cv2.imshow("Andorid Camera", img)

    if cv2.waitKey(1) == 27:
        break # the purpose of this "if" is to shorten the closing conversation when you press the "q" that we did before

cv2.destroyAllWindows()