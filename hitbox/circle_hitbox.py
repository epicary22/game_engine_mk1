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
		is_on: bool = True
		):
		"""
		
		:param radius: The radius of the circle.
		:param center: The center point of the circle.
		:param is_on: Whether the hitbox is active or not.
		"""
		super().__init__(dimensions=(radius * 2, radius * 2), center=center, is_on=is_on)
		

# TODO class defining a circular hitbox.
