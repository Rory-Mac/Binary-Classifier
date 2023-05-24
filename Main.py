from BinaryClassifier import BinaryClassifier
from TrainingSetGenerator import TrainingSetGenerator

if __name__ == "__main__":
    input_count = 2
    learning_rate = 0.1
    number_of_epochs = 100
    training_set = TrainingSetGenerator.convert_ascii_2d("training_set1.txt") 
    binaryClassifier = BinaryClassifier(input_count, learning_rate)
    for index in range(number_of_epochs):
        success_rate = binaryClassifier.train_classifier(training_set)
        print(str(success_rate), end=" ")