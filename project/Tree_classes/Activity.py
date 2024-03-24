class Activity():
    def __init__(self, children):
        self.children = children

    def to_json(self):
        array = []
        for child in self.children:
            array.append(child.to_json())
        dict = {'type': 'Activity', 'children': array}
        return dict