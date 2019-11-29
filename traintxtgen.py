import os
import cv2
import time
img = cv2.imread('/mnt/c/WORKS/ComputerVision/tunghimdataset/data/2.jpg')
print(img.shape)

#Generate train.txt file

cnt = 1
h = 1944
w = 2592

for i in range(1,701):
    print(cnt)
    dir = open('train.txt', 'a')
    dir.write('/mnt/c/WORKS/ComputerVision/tunghimdataset/data/' + str(cnt) + '.jpg ')

    with open('/mnt/c/WORKS/ComputerVision/tunghimdataset/labels/' + str(cnt) + '.txt', 'r') as labels:
        for line in labels:
            numbers = [num for num in line.split()]
            bbox_width = float(numbers[3]) * w
            bbox_height = float(numbers[4]) * h
            center_x = float(numbers[1]) * w
            center_y = float(numbers[2]) * h
            x_min = int(round(center_x - (bbox_width / 2), 0))
            y_min = int(round(center_y - (bbox_height / 2), 0))
            x_max = int(round(center_x + (bbox_width / 2), 0))
            y_max = int(round(center_y + (bbox_height / 2), 0))
            label = numbers[0]
            print('{},{},{},{},{}'.format(x_min,y_min,x_max,y_max,label))
            dir.write('{},{},{},{},{} '.format(x_min,y_min,x_max,y_max,label))
            # dir.write('\n')
            # print(numbers[1])
            # time.sleep(3)
    labels.close()
    dir.write('\n')
    dir.close()
    
    cnt = cnt + 1
