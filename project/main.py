from slojno.project.Tree_classes.Activity import Activity
from slojno.project.Tree_classes.Div import Div
from slojno.project.Tree_classes.Text import Text
from json import dumps

text1 = Text(3)
text2 = Text(2)
text3 = Text(1)
sample_text = Text(1)
div1 = Div([text1, text2, text3], 2)
important_div = Div([sample_text], 1)
activity = Activity([div1, important_div])
json_data = dumps(activity.to_json())

F = open("slojno/project/sample_json.json", "w")
F.write(json_data)
