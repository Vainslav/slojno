from Tree_classes.Node import Node


class Button(Node):
    def __init__(self, text, action_src, width=None, height=None, isvisible=True):
        super().__init__(width, height, isvisible)
        self.text = text
        self.actions['on_click'] = action_src

    def to_json(self):
        dict = super().to_json()
        dict['text']=self.text
        return dict
