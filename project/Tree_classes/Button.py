from slojno.project.Tree_classes.Node import Node


class Button(Node):
    def __init__(self, wight, height, action_src=None, isvisible=True):
        super().__init__(wight, height, isvisible)
        self.actions['on_click'] = action_src
