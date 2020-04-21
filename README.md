# Emergency Driver Alert (EVA) software repository
### This is a project led by Gabriel Sarch, Sylvester Benson-Sesay, and Phuc Do as part of the University of Rochester Biomedical Engineering Senior Design Project
### The problem was pitched to us by Marlene Sutliff and Steven Barnett, UR Community/Deaf Wellness Center and Dan Brooks, President HLAA NYS Association

Problem statement: There is a need to ensure that drivers are alerted of approaching emergency vehicles so that they can quickly and safely remove themselves from the path of the emergency vehicle. It is especially a challenge for deaf, hard of hearing, and distracted drivers to identify emergency signals, which puts them at an increased risk for colliding with emergency vehicles. The focus of this project is to develop a device for use in the car that detects emergency vehicles and notifies the driver of their presence in real time. 

**The code in this repository can be used to train and implement a real-time siren detector** 

## About the detector
The detector is a convolutional neural network (CNN) trained on sirens embedded in urban and car noise

###Video of working detector (click the image to go to video):


[![Alt text](https://img.youtube.com/vi/yw6vhPHvPNU/0.jpg)](https://www.youtube.com/watch?v=yw6vhPHvPNU)

### CNN architecture:
- Four layers convolutional layers (sizes 12, 32, 64, 128) and a fully connected final layer 
- ReLU activation function
- 2x2 filter size
- 20% dropout during training
- last layer has softmax actiavation to get probability of "siren present" and "siren not present"

### Training data
- The training data is taken from UrbanSounds8k data set (https://urbansounddataset.weebly.com/urbansound8k.html), Youtube.com, as well as some field recordings taken in Rochester, NY while driving.
- The CNN is trained on 3 second audio chunks 
- Mel-cepstral frequency coefficients (MFCCs) are extracted and used as input to the CNN
- siren audio and background noise is randomly scrambled before each batch of training 
- Various signal-to-noise ratios between the siren and background noise are generated to increase generalization

## Files in repo
There are four main files:
1) **convertWav2Txt** & **generateTrainingData** are used to format the audio collected, split up the data into chunks, and save it into a numpy array
2) **trainSirenDetector** is for setting up the CNN architecture and training it
3) **Real-Time Siren Detector** is the real-time detector that can be used with any microphone
