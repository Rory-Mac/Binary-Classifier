from BinaryClassifier import BinaryClassifier
from TrainingSetGenerator import TrainingSetGenerator

if __name__ == "__main__":
    input_count = 2
    learning_rate = 0.1
    training_set = TrainingSetGenerator.convert_ascii_2d("example_training_set.txt") 
    binaryClassifier = BinaryClassifier(input_count, learning_rate)
    success_rate = binaryClassifier.train_classifier(training_set)
    print("SUCCESS_RATE: " + str(success_rate))
    success_rate = binaryClassifier.train_classifier(training_set)
    print("SUCCESS_RATE: " + str(success_rate))