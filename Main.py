from BinaryClassifier import BinaryClassifier
from TrainingSetGenerator import TrainingSetGenerator

"""Main function

This module is the endpoint for the client, who can specify the file to be used as a training set, the number of epochs 
used to train the model, the learning rate of the model, and the number of dimensions in the input space.

"""
if __name__ == "__main__":
    input_count = 2
    learning_rate = 0.1
    number_of_epochs = 100
    training_set = TrainingSetGenerator.convert_ascii_2d("training_set1.txt") 
    binaryClassifier = BinaryClassifier(input_count, learning_rate)
    for index in range(number_of_epochs):
        success_rate = binaryClassifier.train_classifier(training_set)
        print(str(success_rate), end=" ")