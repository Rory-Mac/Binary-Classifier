class TrainingSetGenerator:
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
