from Node import Node


class Button(Node):
    def __init__(self, action_src, width=None, height=None, isvisible=True):
        super().__init__(width, height, isvisible)
        self.actions['on_click'] = action_src
