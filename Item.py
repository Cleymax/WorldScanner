class Item:
    def __int__(self, material, count):
        self.material = material
        self.count = count
        self.data = 0

    def __init__(self, material, count, data):
        self.material = material
        self.count = count
        self.data = data
