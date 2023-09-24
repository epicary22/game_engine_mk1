import json
import pygame as pg


class Level:
	JSON_STRUCTURE = {
		"screen_dimensions": (0, 0),
		"objects": {}
	}
	
	def __init__(self, json_filepath):
		self.json_filepath = json_filepath
		self.data = None
		self._parse_json()
		
	def _parse_json(self):
		with open(self.json_filepath, "r") as json_data:
			self.data = json.load(json_data)
			
	def handle_events(self, keys_down, mouse_state):
		pass
		