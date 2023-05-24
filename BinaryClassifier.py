import random
import numpy as np

class BinaryClassifier:
    def __init__(self, input_count, learning_rate):
        self.learning_rate = learning_rate
        self.omega_vector = np.zeros(input_count)
        self.bias = 0
        
    def train_classifier(self, training_set):
        inputs_classified = 0
        inputs_classified_correctly = 0
        for input_tuple in training_set:
            if (self.classify_input(input_tuple[0], input_tuple[1])):
                inputs_classified_correctly += 1
            inputs_classified += 1
        return (100 * (inputs_classified_correctly / inputs_classified))

    def classify_input(self, input_vector, target_classification): 
        result = sum(np.multiply(self.omega_vector, input_vector)) + self.bias
        classification = 1 if result >= 0 else 0
        # handle misclassification
        if classification == 0 and target_classification == 1:
            self.__update_omega_vector(input_vector, 1)
            return False
        if classification == 1 and target_classification == 0:
            self.__update_omega_vector(input_vector, -1)
            return False
        return True

    def __update_omega_vector(self, input_vector, d):
        for index in range(len(self.omega_vector)):
            self.omega_vector[index] += (d * (self.learning_rate * input_vector[index]))
            self.bias += (d * self.learning_rate)