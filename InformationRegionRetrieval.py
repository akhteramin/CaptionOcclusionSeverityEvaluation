import argparse
from imageai.Detection.Custom import CustomObjectDetection

ap = argparse.ArgumentParser()
ap.add_argument("-j", "--img_name", required=True, help="image name")
args = vars(ap.parse_args())

def informationRegionRetrieval():
    print(args.get("img_name"))
    detector = CustomObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath("Dataset_V2/models/detection_model-ex-065--loss-0013.210.h5")
    detector.setJsonPath("Dataset_V2/json/detection_config.json")
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=args.get("img_name"), output_image_path="Output_Frames/"+args.get("img_name"))
    for detection in detections:
        print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])

informationRegionRetrieval()