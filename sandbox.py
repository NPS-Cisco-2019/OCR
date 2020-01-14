import cv2 as cv
import sys, base64, os
import regex as re
import pytesseract
import numpy as np
import text_cropping
from config import *
import argparse

sys.path.append(os.path.join(os.getcwd(), "OCR"))


img = "images/1.png"


def main(img):
    osd = pytesseract.image_to_osd(img)
    angle = re.search("(?<=Rotate: )\d+", osd).group(0)
    script = re.search("(?<=Script: )\d+", osd).group(0)
    print("angle: ", angle)
    print("script: ", script)


if __name__ == "__main__":
    main(img)
