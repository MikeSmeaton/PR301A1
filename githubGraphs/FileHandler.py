class FileHandler(object):
    def __init__(self, file):
        self.file = file

    def get_file(self):
        with open(self.file) as txt_file:
            half_split = []
            for line in txt_file:
                count = 0
                half_split = line.split(' ^ ')
                for arrays in half_split:
                    half_split[count] = half_split[count].split(',')
                    count += 1

            return half_split

    def write_file(self, input_content):
        open_file = open(self.file, "w")
        open_file.write(input_content)
        open_file.close()
        return input_content
