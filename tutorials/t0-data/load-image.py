
from PIL import Image
import cv2
import numpy as np


def main():
    
    # load the image
    img = Image.open("data/img.jpg")

    # get pixel information of data
    img_arr = np.array(img)

    # display the image
    cv2.imshow("img", img_arr)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
