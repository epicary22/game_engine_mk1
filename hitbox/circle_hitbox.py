import pygame as pg
from hitbox.hitbox import Hitbox
from hitbox.rect_hitbox import RectHitbox
import math


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
		) -> None:
		"""
		Defines a circular hitbox.
		:param radius: The radius of the circle.
		:param center: The center point of the circle.
		:param is_on: Whether the hitbox is active or not.
		:param rounding: Whether the hitbox floor-rounds all of its values or not.
		"""
		super().__init__(dimensions=pg.Vector2(radius * 2, radius * 2), center=center, is_on=is_on, rounding=rounding)

	def distance_to(self, other_circle: CircleHitbox) -> bool:
		pass  # TODO find distance function between a circle and a circle, and a circle and a rect.
