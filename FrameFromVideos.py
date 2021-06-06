import cv2
import os
import argparse

from InformationRegionRetrieval import informationRegionRetrievalFromImage

ap = argparse.ArgumentParser()
ap.add_argument("-video_c", "--video_c", required=True, help="video with caption name")
ap.add_argument("-video_nc", "--video_nc", required=True, help="video without caption name")


args = vars(ap.parse_args())
vidcap = cv2.VideoCapture('Test_Videos/'+args.get('video_c'))
vidncap = cv2.VideoCapture('Test_Videos/'+args.get('video_nc'))

success, image = vidcap.read()
count = 0
while success:
  path = 'Test_Images/Captioned'
  cv2.imwrite(os.path.join(path,"frame_c%d.jpg" % count), image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

success_nc, image_nc = vidncap.read()
count = 0
while success_nc:
  path = 'Test_Images/Uncaptioned'
  cv2.imwrite(os.path.join(path,"frame_nc%d.jpg" % count), image_nc)     # save frame as JPEG file
  success_nc,image_nc = vidncap.read()
  print('Read a new frame: ', success_nc)
  count += 1
#
for image_index in range(count):
  informationRegionRetrievalFromImage(os.path.join('Captioned', "frame_c%d.jpg" %image_index), os.path.join("Uncaptioned", "frame_nc%d.jpg" %image_index), image_index)