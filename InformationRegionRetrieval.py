import argparse
from imageai.Detection.Custom import CustomObjectDetection
from imageai.Detection.Custom import CustomVideoObjectDetection
import os

ap = argparse.ArgumentParser()
ap.add_argument("-img_with_caption", "--img_with_caption", required=True, help="image name")
ap.add_argument("-img_without_caption", "--img_without_caption", required=True, help="image name")

args = vars(ap.parse_args())

# Lip motion analysis to detect currnt speaker:
# https://www.researchgate.net/publication/221111889_Visual_Speech_Recognition_with_Loosely_Synchronized_Feature_Streams
def box_area(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    # compute the area of intersection rectangle
    interArea = abs(max((xB - xA, 0)) * max((yB - yA), 0))
    if interArea == 0:
        return 0
    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = abs((boxA[2] - boxA[0]) * (boxA[3] - boxA[1]))
    boxBArea = abs((boxB[2] - boxB[0]) * (boxB[3] - boxB[1]))


    # areas - the interesection area
    # iou = interArea / float(boxAArea + boxBArea - interArea)
    iou = interArea/ float(boxBArea)
    # return the intersection over union value
    return iou

def informationRegionRetrievalFromImage():
    print(args.get("img_name"))
    # Objects = []
    # model configuration
    detector = CustomObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath("Dataset_V2/models/detection_model-ex-070--loss-0015.701.h5")
    detector.setJsonPath("Dataset_V2/json/detection_config.json")
    detector.loadModel()
    # detect objects from an image without caption on the screen
    detections = detector.detectObjectsFromImage(input_image=args.get("img_without_caption"), output_image_path="Output_Frames/"+args.get("img_without_caption"))

    # detect caption from an image with caption on the screen
    caption_detections = detector.detectObjectsFromImage(input_image=args.get("img_with_caption"),
                                                 output_image_path="Output_Frames/" + args.get("img_with_caption"))

    for detection in caption_detections:
        if detection["name"] == "caption":
            print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
            print(type(detection["box_points"]))
            #save boxpoint for caption
            Caption = detection["box_points"]

    result_file = open("result.txt", "w+")
    for detection in detections:
        if detection["percentage_probability"]>=90:

            print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
            # Objects.append(detection["box_points"])

            print(box_area(Caption, detection["box_points"]))
            area = box_area(Caption, detection["box_points"])
            result_file.write(detection["name"] + "- Occlusion Area with Caption: " + str(area)+"\n")



informationRegionRetrievalFromImage()