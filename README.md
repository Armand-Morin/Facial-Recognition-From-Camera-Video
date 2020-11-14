## Facial Recognition From Camera/Video
 This project is in python code which allows to detect the person present in front of a web cam or in a video.

## How to  use

- First, you start the dataset_Creator.py program with the command:
``` bash
python dataset_Creator.py
```
This will ask you for an ID (which should be taken as your name) and then the code starts your Webcame and takes 20 photos of you which it stores in the dataSet folder.
 
 - Then you start the learning phase with the following command:
``` bash
python trainner.py
```
which creates a file in the trainner folder which contains all the characteristics that can be used to characterize an image.

- Then you can finally run ``` bash python detector.py```
which detects the faces of the people he has learned when it starts the webcam.
