
# PoultryDetectuion
For bachelor thesis, drone based poultry detection

### Image scrubbing helper for dataset
For basic image scrubbing from the internet use the ImageScrubbing.py

    keyword = ["chicken on field"] # you can adjust the keywords used for search
    response().download(kw, 50)  # and you can adjust amount of images to download
   
## Anaconda environment
Anaconda software helps you create an environment for many different Python versions and package versions.  Anaconda is also used to install, remove, and upgrade packages in a project environment.  This helps create an isolated environment, which is necessary because different packages depend on different versions of packages for other needs.  environment helps prevent package incompatibility that may occur from other projects, for example installing a newer version of pytorch for ssd neural network may cause an older version of pytorch to no longer work for yolo neural network.  Work with conda is mostly done using the anaconda command line.

![image](https://github.com/Vyzex29/PoultryDetectuion/assets/27866166/21ef3940-e1a6-49fd-820e-f28744e034d9)

most common commands:  

 - "conda info --envs" - prints all created environments in the   
   operating system 
   
 - "conda activate 'environment name'" – activates   
   setting the environment as a working environment 
 - "conda create -n  'environment name' python=3.9" – creates an environment with the -n
   flag specifying the environment name and python=3.9 specifying which
   version of python to install in the isolated environment


After creating and activating the environment, pytorch must be installed with the correct version of cuda.  For yolov7 pytorch must be (torch>=1.7.0,!=1.12.0) which means it must be higher than 1.7.0 but not higher than 1.12.0.  The compatibility table can be found on the official pytorch website.  Yolov7 has a requirements txt file that can be used to install dependencies via the conda command line using the “pip install -r requirements.txt” command.

![image](https://github.com/Vyzex29/PoultryDetectuion/assets/27866166/8112e53e-01c4-4631-9957-23a4501ee88d)

## Main GUI
For the GUI, you need to run Main.py in yolov7Model folder
Demonstration video in latvian: https://youtu.be/UJDGhyHC4Qg

## Trained models
My trained models are available here:

 - Yolov7tiny as base: https://drive.google.com/file/d/1uReXOLnNa5VBZbdG2V_wUuIItCcdQJ3o/view?usp=sharing
 - Yolov7 regular as base: https://drive.google.com/file/d/19oOh4G37N6xURT_tMED4KQ3KAafyAzgq/view?usp=share_link

You can download them and place them in yolov7model/trainedModels, which then can be utilized in the main app.

## Used Dataset for training
Image set: https://drive.google.com/file/d/1tsyVf1yME5edXBDtj9cOpiXxSWfYx9f_/view?usp=share_link
