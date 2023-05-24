import random
import numpy as np

"""BinaryClassifier

This module closely parallels the structure of a perceptron and acts as a binary classifier by defining the public methods 
train_classifier() and classify_input() which together implement the perceptron learning algorithm.

"""
class BinaryClassifier:
    """
    :param input_count: number of input features (number of input edges to a perceptron), defines n-dimensional input space 
    :type input_count: int 
    :param learning_rate: can be modified to find a desirable balance between efficiency and overshooting 
    :type learning_rate: float
    :returns: new BinaryClassifier object
    """
    def __init__(self, input_count, learning_rate):
        self.learning_rate = learning_rate
        self.omega_vector = np.zeros(input_count)
        self.bias = 0
        
    """
    :param training_set: list of tuples containing an n-dimensional input vector as a first entry, 
        and a label (a target classification) as a second entry
    :type training_set: list
    :returns: successful classification by model as a percentage of total classifications made
    """
    def train_classifier(self, training_set):
        inputs_classified = 0
        inputs_classified_correctly = 0
        for input_tuple in training_set:
            if (self.__classify_input(input_tuple[0], input_tuple[1])):
                inputs_classified_correctly += 1
            inputs_classified += 1
        return (100 * (inputs_classified_correctly / inputs_classified))

    """
    :param input_vector: list of individual input values that can be thought of as coordinates in an input space
    :type input_vector: list
    :returns: boolean expression of whether classification was successful or if input was misclassified
    """
    def __classify_input(self, input_vector, target_classification): 
        result = sum(np.multiply(self.omega_vector, input_vector)) + self.bias
        classification = 1 if result >= 0 else 0
        if classification == 0 and target_classification == 1:
            self.__update_omega_vector(input_vector, 1)
            return False
        if classification == 1 and target_classification == 0:
            self.__update_omega_vector(input_vector, -1)
            return False
        return True

    """
    :param input_vector: list of individual input values that can be thought of as coordinates in an input space
    :type input_vector: list
    :param d: used to mathematically simplify difference between increasing and decreasing the gradient of the 
        coordinate to be changed in the event of misclassification, essentially determines whether hyperplane 
        approaches or distances itself from the misclassified input.
    :type int (1 or -1 exclusively)
    """
    def __update_omega_vector(self, input_vector, d):
        for index in range(len(self.omega_vector)):
            self.omega_vector[index] += (d * (self.learning_rate * input_vector[index]))
            self.bias += (d * self.learning_rate)