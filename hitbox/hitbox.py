import pygame as pg
import math


class Hitbox:
	def __init__(
		self,
		dimensions: pg.Vector2,
		left_top: pg.Vector2 = None,
		center: pg.Vector2 = None,
		is_on: bool = True,
		rounding: bool = True
	) -> None:
		"""
		Base hitbox class.
		:param dimensions: The size of the hitbox in the x, then y direction.
		:param left_top: The top-left coordinate of the rectangle the hitbox fits inside.
		:param center: The center point of the hitbox.
		:param is_on: Whether the hitbox is active or not.
		:param rounding: Whether the hitbox floor-rounds all of its values or not.
		"""
		self.is_on = is_on
		self.rounding = rounding
		
		self.dimensions = dimensions
		self.left_top = left_top
		self.center = center
		
		if self.rounding:
			self.dimensions = self._round_vector2(self.dimensions)
			if self.left_top:
				self.left_top = self._round_vector2(self.left_top)
			if self.center:
				self.center = self._round_vector2(self.center)
			
		if not self.center and not self.left_top:
			raise Exception("Did not provide a pair of center or a left-top coordinates.")
		elif not self.left_top:
			self._calculate_left_top()
		elif not self.center:
			self._calculate_center()
		else:
			raise Exception("Cannot process both center and left-top values given.")
		if self.rounding:
			self._round_position()
		
		self.print_pos_stats()
		
	def _calculate_center(self) -> None:
		"""
		Calculates the center coordinate of the hitbox using the left-top and dimensionsd.
		"""
		center_x = self.left_top.x + 0.5 * self.dimensions.x
		center_y = self.left_top.y + 0.5 * self.dimensions.y
		self.center = pg.Vector2(center_x, center_y)
	
	def _calculate_left_top(self) -> None:
		"""
		Calculates the left-top coordinate of the hitbox using the center and dimensions.
		"""
		left_x = self.center.x - 0.5 * self.dimensions.x
		top_y = self.center.y - 0.5 * self.dimensions.y
		self.left_top = pg.Vector2(left_x, top_y)
		
	def _round_position(self) -> None:
		"""
		Floor-rounds the left-top and center coordinates of the hitbox.
		"""
		self.left_top = self._round_vector2(self.left_top)
		self.center = self._round_vector2(self.center)
	
	@staticmethod
	def _round_vector2(vector2) -> pg.Vector2:
		"""
		Floor-rounds a Vector2.
		:param vector2: A Vector2.
		:return: The rounded Vector2.
		"""
		return pg.Vector2(vector2.__floordiv__(1))
	
	def print_pos_stats(self) -> None:
		"""
		Prints positional information about the hitbox.
		"""
		print("dimensions: ", self.dimensions.xy, "\nleft-top: ", self.left_top, "\ncenter: ", self.center)
	