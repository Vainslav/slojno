from Tree_classes.Activity import Activity
from Tree_classes.Flexbox import Flexbox
from Tree_classes.Text import Text
from json import dumps


def generate_json():
    activity = Activity("123", [Text("hsakjdhj"), Text("123")])
    json_data = dumps(activity.to_json())

    return json_data

generate_json()