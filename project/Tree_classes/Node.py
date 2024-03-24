class Node():
    def __init__(self, content=None, isvisible = True):
        self.actions = []
        self.content = content
        self.isvisible = isvisible

    def add_action(self, action):
        self.actions.append(action)

    def to_json(self):
        dict = {'type': type(self).__name__, 'actions': self.actions, 'content': self.content, 'isvisible': self.isvisible}
        return dict
