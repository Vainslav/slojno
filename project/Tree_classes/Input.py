from Node import Node


class Input(Node):
    def __init__(self, action_src, width=None, height=None, isvisible=True):
        super().__init__(width, height, isvisible)
        self.actions['on_change'] = action_src
