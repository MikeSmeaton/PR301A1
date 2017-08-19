class FileHandler(object):
    def __init__(self, file):
        self.file = file

    def get_file(self):
        open_file = open(self.file, "r")
        print("Opening: ", open_file.name)
        file_array = open_file.read()
        print(file_array)
        open_file.close()
        return file_array

    def write_file(self):
        open_file = open(self.file, "w")
        writing = input("Write file content: ")
        open_file.write(writing)
        print(writing)
        open_file.close()

