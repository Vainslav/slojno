from Tree_classes.Activity import Activity
from Tree_classes.Flexbox import Flexbox
from Tree_classes.Text import Text
from Tree_classes.Button import Button
from Tree_classes.Image import Image
from json import dumps

class Items():
	def __init__(self, name, image, cost):
		self.name = name
		self.image = image
		self.cost = cost
	def makedata(self):
		label = Text(self.name)
		cost = Text(self.cost)
		image = Image(self.image)
		buy_button = Button("купить", "zglush")
		return Flexbox([label, image, cost, buy_button])

def generate_json():
	head_text = Text("КАТАЛОГ")
	
	bkb = Items("BKB", "bkb.png", 4050)
	prischepka = Items("Прищепка", "prischepka.png", 999)
	magic_wand = Items("Magic Wand", "magic_wand.png", 450)
	
	head = Flexbox([head_text])

	activity_basket = Activity("basket", [])
	activity_main = Activity("main", [bkb.makedata(), prischepka.makedata(), head])
    
	json_data = dumps(activity_main.to_json())
	F = open("sample_json.json", "w")
	F.write(json_data)
	F.close()
	return open('sample_json.json')

generate_json()
