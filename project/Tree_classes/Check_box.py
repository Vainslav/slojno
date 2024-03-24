from Tree_classes.Node import Node


class Checkbox(Node):
    def __init__(self, action_src, width=None, height=None, isvisible=True):
        super().__init__(width, height, isvisible)
        self.actions['on_switch'] = action_src
