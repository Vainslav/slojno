from slojno.project.Tree_classes.Node import Node


class Checkbox(Node):
    def __init__(self, wight, height, action_src,  isvisible=True):
        super().__init__(wight, height, isvisible)
        self.actions['on_switch'] = action_src
