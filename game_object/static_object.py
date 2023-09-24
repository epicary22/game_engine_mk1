from game_object.game_object import GameObject


class StaticObject(GameObject):
	JSON_STRUCTURE = {
		"name": "",
		"on_collide": "collide/kill/event",
		"hitbox_shape": "rect/circle",
		"hitbox_left_top": (0, 0),
		"hitbox_xy_size": (0, 0),
		"hitbox_center": (0, 0),
		"hitbox_radius": 0,
		"texture": "./static/foo.png",
		"color_overlay": "#FFFFFFFF"
	}

	def __init__(self, name, collides):
		super().__init__(name)
		self.collides = True  # TODO tells you if the object collides or not.
	
	# TODO an object that doesn't react to any events or move, and can have collisions.
	