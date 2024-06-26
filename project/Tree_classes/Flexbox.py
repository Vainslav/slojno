from Tree_classes.Node import Node


class Flexbox(Node):
    def __init__(self, data, height=None, width=None,  flex_flow='row nowrap', justify_content='flex-start', align_items='stretch', align_content='normal', isvisible=True):
        super().__init__(width, height, isvisible)
        self.data = data
        self.flex_flow = flex_flow
        self.justify_content = justify_content
        self.align_items = align_items
        self.align_content = align_content

    def to_json(self):
        array = []
        dict = super().to_json()
        if self.data:
            for child in self.data:
                array.append(child.to_json())
        dict1 = {'flex_flow': self.flex_flow, 'justify_content': self.justify_content, 'align_items': self.align_items, 'align_content': self.align_content, 'isvisible': self.isvisible, 'data': array}
        dict.update(dict1)
        return dict
