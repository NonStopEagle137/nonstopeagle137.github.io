import cv2
import os
from glob import glob

def byNumber(path):
    number = int(eval(path.split(os.path.sep)[-1].split('.png')[0]))
    return number


image_folder = '/media/athrva/New Volume/cis520/Final Project/frameSequence5'#'/home/athrva/Desktop/UnsupervisedClustering/u_sup3'
video_name = 'photo2map.avi'

images = sorted(glob(image_folder + os.path.sep + '*.png'), key = byNumber)
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 15, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()