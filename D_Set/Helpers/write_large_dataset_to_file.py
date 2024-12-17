class Writer:
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, data):
        with open(self.file_path, 'w') as file:
            for row in data:
                file.write(row)
                file.write('\n')