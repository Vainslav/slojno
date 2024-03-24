from slojno.project.Tree_classes.Node import Node


class Button(Node):
    def __init__(self, text, action_src, wight=None, height=None, isvisible=True):
        super().__init__(wight, height, isvisible)
        self.text = text
        self.actions['on_click'] = action_src
