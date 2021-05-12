from imageai.Detection.Custom import DetectionModelTrainer

def modelTraining():
    trainer = DetectionModelTrainer()
    trainer.setModelTypeAsYOLOv3()
    trainer.setDataDirectory(data_directory="Dataset_V2")
    trainer.setTrainConfig(object_names_array=["caption","logo","speaker name", "speaker title",
                                           "discussion topic","current time and temperature", "speaker location",
                                           "scrolling news","program title", "weather map", "social network handle",
                                           "speaker eyes", "speaker mouth", "listener face"],
                           batch_size=4, num_experiments=100, train_from_pretrained_model="pretrained-yolov3.h5")
    trainer.trainModel()

modelTraining()