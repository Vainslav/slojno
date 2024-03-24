from slojno.project.Tree_classes.Node import Node


class Div(Node):
    def __init__(self, data, priority):
        super().__init__(priority)
        self.data = data

    def to_json(self):
        array = []
        if self.data:
            for child in self.data:
                array.append(child.to_json())
        dict = {'type': 'Div', 'priority': self.priority, 'actions': self.actions, 'data': array}
        return dict
