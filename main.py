import cv2
import os
from yolo_show_annos import get_anno

path = 'C:/Users/batuhan/Desktop/first 5000 renamed/'

files = os.listdir(path)
paths = []
bbox = []

for file in files:
    arr = file.split('.')

    if arr[0] not in paths:
        paths.append(arr[0])

for plain_path in paths:
    image = get_anno(path + plain_path)
    cv2.imshow('image', image)

    k = cv2.waitKey(0)
    if k == 115:
        os.remove(path + plain_path + '.jpg')
        os.remove(path + plain_path + '.txt')
    if k == 107:
        continue

cv2.destroyAllWindows()