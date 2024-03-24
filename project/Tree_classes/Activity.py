from slojno.project.Tree_classes.Flexbox import Flexbox


class Activity(Flexbox):
    def __init__(self, name, data, wight=None, height=None,  flex_flow='row nowrap', justify_content='flex-start', align_items='stretch', align_content='normal'):
        super().__init__(wight, height, data, flex_flow, justify_content, align_items, align_content)
        self.name = name

    def to_json(self):
        dict = super().to_json()
        dict['name'] = self.name
        return dict
