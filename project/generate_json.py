from slojno.project.Tree_classes.Activity import Activity
from slojno.project.Tree_classes.Flexbox import Flexbox
from slojno.project.Tree_classes.Text import Text
from json import dumps

class Option():
	def __init__(self, name, image, cost):
		self.name = name
		self.image = image
		self.cost = cost
	def makedata(self):
		label = Text(self.name)
		cost = Text(self.cost)
		image = Image(self.image)
		buy_button = Button()
		return Flexbox(label, image, cost, button)

def generate_json():

	bkb = Option("BKB", "bkb.png", 4050)
	prischepka = Option("Прищепка", "prischepka.png", 999)
	magic_wand = Option("Magic Wand", "magic_wand.png", 450)

    activity_basket = Activity("basket", )
    activity_main = Activity("main", [bkb.makedata(), prischepka.makedata()])
    
    json_data = dumps(activity.to_json())

    F = open("sample_json.json", "w")
    F.write(json_data)
    F.close()
    return open('sample_json.json')

generate_json()
