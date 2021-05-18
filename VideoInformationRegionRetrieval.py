import argparse
from imageai.Detection.Custom import CustomObjectDetection
from imageai.Detection.Custom import CustomVideoObjectDetection
import os

# ap.add_argument("-j", "--vid_name", required=False, help="video name")

# args = vars(ap.parse_args())

# def forFrame(frame_number, output_array, output_count):
#     print("FOR FRAME ", frame_number)
#     print("Output for each object : ", output_array)
#     print("Output count for unique objects : ", output_count)
#     print("————END OF A FRAME ————–")
#
# def informationRegionRetrievalFromVideo():
#     execution_path = os.getcwd()
#
#     video_detector = CustomVideoObjectDetection()
#     video_detector.setModelTypeAsYOLOv3()
#     video_detector.setModelPath("Dataset_V2/models/detection_model-ex-070--loss-0015.701.h5")
#
#     video_detector.setJsonPath("Dataset_V2/json/detection_config.json")
#     video_detector.loadModel()
#
#     video_detector.detectObjectsFromVideo(input_file_path="holo1.mp4",
#                                           output_file_path=os.path.join(execution_path, "holo1-detected"),
#                                           frames_per_second=30,
#                                           minimum_percentage_probability=40,
#                                           log_progress=True,
#                                           per_frame_function=forFrame)
