from slojno.project.Tree_classes.Flexbox import Flexbox


class Activity(Flexbox):
    def __init__(self, data, flex_flow='row nowrap', justify_content='flex-start', align_items='stretch', align_content='normal'):
        super().__init__(data, flex_flow, justify_content, align_items, align_content)
