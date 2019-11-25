class File:
    def __init__(self):
        pass
    # def __init__(self, name, data):
    #     try:
    #         with open(name, "x") as self.file:
    #             self.file.write(data)
    #             self.file.close()
    #     except IOError:
    #         print("File already exists")

    def create(self, name):
        try:
            with open(name, "x") as self.file:
                pass
        except IOError:
            print("File already exists")


