from Tree_classes.Node import Node


class Input(Node):
    def __init__(self, action_src, wight=None, height=None, isvisible=True):
        super().__init__(wight, height, isvisible)
        self.actions['on_change'] = action_src
