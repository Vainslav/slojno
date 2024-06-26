from Tree_classes.Node import Node


class Text(Node):
    def __init__(self, content, width=None, height=None, isvisible=True):
        super().__init__(width, height, isvisible)
        self.content = content

    def to_json(self):
        dict = super().to_json()
        dict['content'] = self.content
        return dict
