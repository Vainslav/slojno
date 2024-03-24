from slojno.project.Tree_classes.Activity import Activity
from slojno.project.Tree_classes.Flexbox import Flexbox
from slojno.project.Tree_classes.Text import Text
from json import dumps


def generate_json():
    text1 = Text('just text')
    text2 = Text('sample text')
    text3 = Text('some text')
    flexbox1 = Flexbox([text1, text2, text3])
    important_flexbox = Flexbox([flexbox1])
    activity = Activity("popa", [flexbox1, important_flexbox])
    json_data = dumps(activity.to_json())

    F = open("sample_json.json", "w")
    F.write(json_data)
    F.close()
    return open('sample_json.json')

generate_json()