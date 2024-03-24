from slojno.project.Tree_classes.Activity import Activity
from slojno.project.Tree_classes.Flexbox import Flexbox
from slojno.project.Tree_classes.Text import Text
from json import dumps


def generate_json():
    activity = Activity()
    json_data = dumps(activity.to_json())

    F = open("sample_json.json", "w")
    F.write(json_data)
    F.close()
    return open('sample_json.json')

generate_json()