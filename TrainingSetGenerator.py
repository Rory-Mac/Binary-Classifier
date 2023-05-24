"""TrainingSetGenerator

This module acts as a mediator between the file_resources folder containing datasets, and the training sets used to train the binary 
classifier. The module is static, and simply contains a set of static class functions that convert from a binary or ascii data format to 
a tuple-based training set to be interpreted by the BinaryClassifier class. Open to extension to account for more formats.

"""
class TrainingSetGenerator:
    """Convert ascii expression of dataset (best used for visual demonstration) into a suitable training set
    :param file_name: name of file located in file_resources folder 
    :type file_name: String
    :returns: new training set to be processed by BinaryClassifier
    """
    @classmethod
    def convert_ascii_2d(self, file_name):
        input_tuples = []
        file = open(('file_resources/' + file_name))
        x = 0
        y = 0
        while True:
            char = file.read(1)
            if char == "\n":
                x = 0
                y += 1
                continue
            if not char:
                break
            input_tuples.append(([x,y], (0 if char == "0"else (1 if char == "1" else None))))
            x += 1
        file.close()
        return input_tuples
