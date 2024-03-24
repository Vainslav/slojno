from Tree_classes.Flexbox import Flexbox


class Activity(Flexbox):
    def __init__(self, name, data, width=None, height=None,  flex_flow='row nowrap', justify_content='flex-start', align_items='stretch', align_content='normal'):
        super().__init__(data, width, height, flex_flow, justify_content, align_items, align_content)
        self.name = name

    def to_json(self):
        dicta = super().to_json()
        dicta['name'] = self.name
        return dicta
