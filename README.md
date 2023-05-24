# Binary-Classifier
This repository contains an object-oriented-programming package that performs binary classification on any n-dimensional linearly-separable dataset (provided that 
the dataset has been preprocessed by the client application into binary form). It can be used for demonstration in introductory neural network and machine learning courses in tertiary education, or as a visual study tool for any individual who wishes to better understand the workings of binary classification. Some parameters to look for in Main.py include:
- number_of_epochs (how many rounds of training the model will undertake in learning how to classify the dataset optimally)
- learning_rate (a balance-beam value between the model's learning efficiency and the degree to which it overshoots)
- input_count (how many dimensions the input space exists on, or put more simply, how many )
- filename (filename of client-defined dataset; requires additional definition of conversion function in TrainingSetGenerator.py)
Additionaly, the self.omega_vector and self.bias variables in BinaryClassifier.py can be modified to make it easier or harder for the 
model to arrive at the parameter-set that allows for efficient learning.