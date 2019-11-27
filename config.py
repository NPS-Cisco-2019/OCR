import numpy as numpy
import cv2 as cv
import pytesseract
import sys, base64, os

TESTING = True

def fileLog(*vals):
    with open('OCR_progress_log.txt', 'a+') as f: 
        f.write(''.join(str(elem) for elem in vals) + '\n')

if TESTING:
    log = print
else:
    log = fileLog


def initLog():
    open('OCR_progress_log.txt', 'w').close()

sys.path.append(os.path.join(os.getcwd(), "OCR"))
print(sys.path)

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Student\AppData\Local\Tesseract-OCR\tesseract.exe"

