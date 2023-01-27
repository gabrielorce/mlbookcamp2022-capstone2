# Multiclass Image detection: Electronics Components

## ML Zoomcamp - Capstone Project


Below is a description for the 2nd capstone project for the Machine Learning Zookcamp - 2022 cohort. The project consists of a Multiclass Image detection for Electronics Components.

The course can be found here: https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/cohorts/2022

## Problem Description and proposed solution:
The idea for this system is to be able to identify if any specific electronic components appear in an image. These components are:
- LED
- resistor
- push button
- potentiometer
- ultrasonic sensor


To achieve this, we train a CNN to learn the components' visual structures, so that when a new image is presented the component can be correctly identified. As a first approach, we use the Xception Keras Application and transfer learning as a base, and train from there on. The convolutional layers remain untouched, and training will happen at the deep layers.
The Xception Keras Application can be found here: https://keras.io/api/applications/xception/

The dataset we use for training and testing can be found here:
https://www.kaggle.com/datasets/olavomendes/elec-dataset

## Using the notebooks
Before using the "electronics_train.ipynb" notebook, you should unzip the dataset in the same directory. This should leave you seeing the "electronics_dataset" folder visible, and within it a "train_set" and a "test_set" folder, each with the images separated in folders that correspond to the above categories.
Executing the notebook will train the neural network.

The "electronics_test.ipynb" notebook allows testing the selected model locally. You can use some sample images that are in the "electronics_dataset" folder you unzipped (these files are in the top level directory, and not in the train or test subfolders), or use files you donwload from the internet.


## Model Deployment
The deployment is done using a container and setting up AWS lambda function and API gateway, which were correctly set up.
The model is created using Tensorflow; but for deployment, we will use tensorflow-lite. Therefore the model created in the previous step needs to be converted from the h5 format to the tflite format. This was achieved using the "convert.py" file, which is the one provided inthe course (only modification: The name of the file to convert). Both the original h5 as well as the converted tflite model are available in this repository (NOTE: It is a better practice to store these as artifacts in an artifact repository or equivalent, since they are large binary files and not really suitable for code versioning system like git).

Once we have the new, lighter model, we create the container that will include the necessary files.
The Dockerfile contains details of what is included (this includes the tflite model). To build this dockerfile, execute the following command:
docker build -t electronics-components-model .

you can run it locally using this command:
> docker run -it --rm -p 8080:8080 electronics-components-model:latest

But ultimately, we actually upload the docker container when creating the AWS Lambda function and use it from within. The course states how to create this Lambda function in AWS via command line, but in my case I did everything through the graphical interface provided by AWS.

## Testing the deployed model
The application can be tested using the test.py file. It contains a call to the AWS lambda function giving as input a URL of an image. Once executed it will return the component labels as well as the probability that what is shown in the image is one of them. Some sample URLs have been placed in that file; they have been commented out, feel free to use them as wanted.
NOTE: There is no need to run notebooks or build anything for testing, since test.py acts on the AWS Lambda function that was already deployed. You can simply run

> python test.py

at any time and it will return the values.

## Future ideas
The model is not perfect and can use improvement. For example, doing more training with a further selection of images would help.

Data augmentation techniques could be used (they were not applied yet because of a HDD limitation on the Saturn Cloud I was using, added to the time limit).

Also - this was only tested using the Xception Keras application; it's very likely there is at least one better model to start from (VGG19 or ResNet50 are sample candidates), so a next step could be to switch to one of these and get results.





