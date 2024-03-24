class Node():
    def __init__(self, priority):
        self.priority = priority
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)

    def to_json(self):
        dict = {'type': type(self).__name__, 'priority': self.priority, 'actions': self.actions}
        return dict
