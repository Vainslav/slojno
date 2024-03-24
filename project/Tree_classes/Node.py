class Node:
    def __init__(self, width=None, height=None, isvisible=True, classes=None):
        self.actions = []
        self.isvisible = isvisible
        self.classes = classes
        self.width = width
        self.height = height

    def to_json(self):
        dict = {'type': type(self).__name__, 'actions': self.actions, 'isvisible': self.isvisible, 'width': self.width, 'height': self.height, 'classes': self.classes}
        return dict
