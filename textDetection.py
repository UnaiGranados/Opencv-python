#Windows: Download tesseract https://github.com/UB-Mannheim/tesseract/wiki
#Ubuntu: sudo apt install tesseract-ocr
#Ubuntu:sudo apt install libtesseract-dev
#Copy
# C:\Program Files\Tesseract-OCR\tessdata

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\Unai\\Downloads\\tesseract-ocr-w64-setup-v5.1.0.20220510.exe"
img = cv2.imread("Resources/text2.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))
cv2.imshow("Result",img)
cv2.waitKey(0)