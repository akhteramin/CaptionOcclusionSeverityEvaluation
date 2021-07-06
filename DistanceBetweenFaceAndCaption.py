import argparse
from imageai.Detection.Custom import CustomObjectDetection
from imageai.Detection.Custom import CustomVideoObjectDetection
import os
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-file_name", "--file_name", required=False, help="file name")
# ap.add_argument("-img_without_caption", "--img_without_caption", required=False, help="image name")
#
args = vars(ap.parse_args())

# Lip motion analysis to detect currnt speaker:
# https://www.researchgate.net/publication/221111889_Visual_Speech_Recognition_with_Loosely_Synchronized_Feature_Streams
def distance_box_area(boxA, boxB):

    distance = min(min(abs(boxA[1]-boxB[1]),abs(boxA[1]-boxB[3])), min(abs(boxA[3]-boxB[3]),abs(boxA[3]-boxB[1])))

    return distance

def extract_frame_from_video(file_name):
    vid = cv2.VideoCapture('Test_Distance/' + file_name)
    success, image = vid.read()
    count=0
    while success:
        if count==90:
            path = 'Test_Distance/'
            cv2.imwrite(os.path.join(path, file_name+".jpg"), image)  # save frame as JPEG file
            return
        success, image = vid.read()
        print('Read a new frame: ', success)
        count += 1
    return

def informationRegionRetrievalFromImage():
    print(args.get("file_name"))
    # print(captioned_image, uncaptioned_image)
    file_name = args.get("file_name")
    extract_frame_from_video(file_name)


    # model configuration
    detector = CustomObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath("Dataset_V2/models/detection_model-ex-070--loss-0015.701.h5")
    detector.setJsonPath("Dataset_V2/json/detection_config.json")
    detector.loadModel()

    # detect caption from an image with caption on the screen
    detections = detector.detectObjectsFromImage(input_image=os.path.join("Test_Distance",file_name+".jpg"),
                                                 output_image_path=os.path.join("Test_Distance", file_name+"_OP.jpg"))
    try:
        for detection in detections:
            if detection["name"] == "caption":
                print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
                print(type(detection["box_points"]))
                #save boxpoint for caption
                Caption = detection["box_points"]
    except:
        print("No caption found")
    try:
        #Face Detection
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # Read the input image
        img = cv2.imread("Test_Distance/"+file_name+".jpg")
        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        print(faces)
        if len(faces)==0:
            faces = [[391,  47,  58,  58]]
        distance = distance_box_area(Caption, faces[0])
        print(distance)

        result_file = open(os.path.join("Test_Distance/Result_Distance", "result_"+ file_name+".txt"), "w+")
        result_file.write("Distance: " + str(distance) + "\n")
    except:
        print("Some error occured.")

informationRegionRetrievalFromImage()