from slojno.project.Tree_classes.Node import Node


class Image(Node):
    def __init__(self, wight, height, content, isvisible=True):
        super().__init__(wight, height, isvisible)
        self.content = content

    def to_json(self):
        dict = super().to_json()
        dict['content'] = self.content
        return dict