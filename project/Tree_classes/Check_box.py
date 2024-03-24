from slojno.project.Tree_classes.Node import Node


class Checkbox(Node):
    def __init__(self, action_src, wight=None, height=None, isvisible=True):
        super().__init__(wight, height, isvisible)
        self.actions['on_switch'] = action_src
