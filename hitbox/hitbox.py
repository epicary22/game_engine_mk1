import pygame as pg


class Hitbox:
	"""
	Base hitbox class.
	"""
	def __init__(
		self,
		dimensions: tuple[float, float],
		left_top: pg.Vector2 = None,
		center: pg.Vector2 = None,
		is_on: bool = True,
	):
		"""
		:param dimensions: The size of the hitbox in the x, then y direction.
		:param left_top: The top-left coordinate of the rectangle the hitbox fits inside.
		:param center: The center point of the hitbox.
		:param is_on: Whether the hitbox is active or not.
		"""
		self.is_on = is_on
		self.dimensions = dimensions
		self.left_top = None
		self.center = None
		if not center and not left_top:
			raise Exception("Did not provide a pair of center or a left-top coordinates.")
		if left_top:
			self.left_top = left_top
		else:
			self._calculate_left_top()
		
	def _calculate_center(self):
		pass
	
	def _calculate_left_top(self):
		pass
	