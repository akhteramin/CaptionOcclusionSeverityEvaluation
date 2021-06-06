from imageai.Detection.Custom import DetectionModelTrainer
def modelEvaluator():
    trainer = DetectionModelTrainer()
    trainer.setModelTypeAsYOLOv3()
    trainer.setDataDirectory(data_directory="Dataset_V2")
    trainer.evaluateModel(model_path="Dataset_V2/models",
                          json_path="Dataset_V2/json/detection_config.json",
                          iou_threshold=0.5, object_threshold=0.3, nms_threshold=0.5)
modelEvaluator()