from slojno.project.Tree_classes.Node import Node


class Service_node(Node):
    def __init__(self, priority, content, has_header=False):
        super().__init__(priority)
        self.content = content
        self.actions = []
        self.has_header = has_header

    def add_action(self, action):
        self.actions.append(action)

    def to_json(self):
        dict = {'type': 'Service_node', 'priority': self.priority, 'actions': self.actions, 'content': self.content.to_json(), 'has_header': self.has_header}
        return dict
