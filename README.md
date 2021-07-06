# Caption Occlusion Severity Evaluation
This is a proposed metric for evaluating a captioned videos based on frame by frame analysis. This analysis includes several visual graphical elements into consideration, e.g. current speakers' face, textual information. The motivation of considering these onscreen elements as a parameter of measuring quality of captioning is people who are Deaf and Hard of Hearing relies on captioning while watching TV programming expressed concerns regarding these graphical elements being blocked by caption. Particularly, while broadcasting live TV programming, broadcasters tend incorporate a lot of onscreen visual items to disseminate time-sensitive information which, on the other hand, makes captioners' ability to place caption in a non-intrusive location challenging. Also in a real-time settings, it is hardly possible for captioners to place captions carefully on a non-intrusive location. Therefore, this is quite common that caption occludes one or several onscreen visual elements together in live TV program. 

It is note that while leaving caption in a traditional location captioners are not aware of which onscreen elements are vital to DHH viewers or which are not. Therefore, there is a need to identify which onscreen elements is prioritized by DHH viewers while watching live captioned TV programs. To shed light on this, in our recent investigation titled "Caption-Occlusion Severity Judgments across Live-Television Genres from Deaf and Hard-of-Hearing Viewers" and published in Web for All (W4A '21) conference, we have determined a dataset of graphical elements prioritized by people who are Deaf and Hard of Hearing while watching live captioned TV programming. 

Here in this project, we aim to employ the dataset of graphical elements develop a computer vision model which might be able to determine which graphical elements is present on the screen at a given time and which onscreen elements being blocked by captions.

Using transfer learning approach, we have trained `YoloV3` model so that this model recognize the information regions(graphical elements) identified in out previous phase of research. In this project, `Dataset_V2` contains `COCO` or XML format annotated images which is then, employed to train our model. 

Here is the step-by-step configuration instructions:
1. Setup a Python Virtaul Environment which will support Python 3.6.

     ```python3 -m venv metric-env```
2. Activate virtual environment.

   ```source metric-env/bin/activate```
3. Install required libraries using `requirements.txt`.

   ```pip install -r requirements.txt```
4. Download the pretrained YoloV3 model.

   ```wget https://github.com/OlafenwaMoses/ImageAI/releases/download/essential-v4/pretrained-yolov3.h5```
5. To initiate the transfer learning, run this command:

   ```python InformationRegionObjectDetectionTrainer.py```

   Current hyperparameters are: batch_size=4, num_experiments=100. The validation loss in each epochs can be observed in verbose.
The model will be saved in `Models` file of `Dataset_V2` directory.
6. At the end of the training, to evaluate the model run this command below:

   ```python InformationRegionObjectDetectionModelEvaluator.py```
7. Now using the best model architecture, we will evaluate a frame of a captioned video. Here are the description of our proposed approach to measure occlusion:
The function expects two image frames from actual video sources. One with captions and other without captions.
Analyzing the frame without caption, our metric will identify the region for different information regions. In region identification, primarily we will consider 0.9 as lower bound probability for each content region.
Analyzing the frame with caption, our metric will identify the coordinates of the caption.
Now, this function will measure the occlusion percentage for each region with the caption region. 

   ```python InformationRegionRetrieval.py --img_with_caption 1_caption.png --img_without_caption 1_no_caption.png```
   
8. The project structure has been modified to effectively analyze videos. We extract frames from each of the videos and stored them in `Output_Frames` folder. Subsequently, using the pretrained object detection model, we analyze the occlusion percentage and generate result in `Results` folder. To execute this pipeline, first we need to store two(one captioned, one uncaptioned) video in `Test_Videos` folder. Then run the command shown below:
    ```python FrameFromVideos.py --video_c captioned.mov --video_nc uncaptioned.mov```

9. Distance calculation between Face and Caption (This command is for processing Bulk files.)
```for f in Test_Distance/*.mov; do  python DistanceBetweenFaceAndCaption.py --file_name ${f##*/}; done ```
