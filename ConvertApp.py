class ConverterApp:
    def __init__(self, root):
        self.root = float(root)

    def convert_and_save(self):
        degrees = self.root * 3.14159 / 180
        return degrees
