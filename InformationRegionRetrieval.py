import argparse
from imageai.Detection.Custom import CustomObjectDetection
from imageai.Detection.Custom import CustomVideoObjectDetection
import os

ap = argparse.ArgumentParser()
ap.add_argument("-j", "--img_name", required=True, help="image name")
ap.add_argument("-j", "--vid_name", required=False, help="video name")

args = vars(ap.parse_args())


def informationRegionRetrievalFromImage():
    print(args.get("img_name"))
    detector = CustomObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath("Dataset_V2/models/detection_model-ex-065--loss-0013.210.h5")
    detector.setJsonPath("Dataset_V2/json/detection_config.json")
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=args.get("img_name"), output_image_path="Output_Frames/"+args.get("img_name"))
    for detection in detections:
        print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])

def forFrame(frame_number, output_array, output_count):
    print("FOR FRAME ", frame_number)
    print("Output for each object : ", output_array)
    print("Output count for unique objects : ", output_count)
    print("————END OF A FRAME ————–")

def informationRegionRetrievalFromVideo():
    execution_path = os.getcwd()

    video_detector = CustomVideoObjectDetection()
    video_detector.setModelTypeAsYOLOv3()
    video_detector.setModelPath("Dataset_V2/models/detection_model-ex-070--loss-0015.701.h5")

    video_detector.setJsonPath("Dataset_V2/json/detection_config.json")
    video_detector.loadModel()

    video_detector.detectObjectsFromVideo(input_file_path="holo1.mp4",
                                          output_file_path=os.path.join(execution_path, "holo1-detected"),
                                          frames_per_second=30,
                                          minimum_percentage_probability=40,
                                          log_progress=True,
                                          per_frame_function=forFrame)



informationRegionRetrievalFromImage()