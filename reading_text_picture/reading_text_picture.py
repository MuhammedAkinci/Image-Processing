from PIL import Image
import pytesseract

img = Image.open("C:\PycharmProjects\Opencv\(r)esimdeki_metni_okuma\(t)ext.png") # no cv2 here we read it like this
text = pytesseract.image_to_string(img, lang="eng")
# here we actually did the reading process, first we entered what to read and then what language to read
print(text)