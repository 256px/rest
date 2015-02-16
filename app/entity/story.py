class Story:

    def __init__(self):
        self.id = 0
        self.title = ''
        self.data = []

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data
