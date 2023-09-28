import pygame as pg
from hitbox import Hitbox


class CircleHitbox(Hitbox):
	"""
	Defines a circular hitbox.
	"""
	def __init__(
		self,
		radius: float,
		center: pg.Vector2,
		is_on: bool = True,
		rounding: bool = True
		):
		"""
		:param radius: The radius of the circle.
		:param center: The center point of the circle.
		:param is_on: Whether the hitbox is active or not.
		:param rounding: Whether the hitbox floor-rounds all of its values or not.
		"""
		super().__init__(dimensions=pg.Vector2(radius * 2, radius * 2), center=center, is_on=is_on, rounding=rounding)
		

# TODO class defining a circular hitbox.
