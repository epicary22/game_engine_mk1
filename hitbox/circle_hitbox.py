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
		self.radius = radius

	def distance_to(self, other_hitbox: Hitbox) -> float:
		"""
		Finds the distance between the outer boundaries of this hitbox and another hitbox.
		:param other_hitbox: Another hitbox. Can be RectHitbox or CircleHitbox.
		:return: The distance between the outer boundaries.
		"""
		if other_hitbox.__class__ == CircleHitbox:
			return self._distance_to_circle(other_hitbox)
		elif other_hitbox.__class__ == RectHitbox:
			return self._distance_to_rect(other_hitbox)
		else:
			raise Exception("Must provide a RectHitbox or CircleHitbox.")
		# TODO find distance function between a circle and a circle, and a circle and a rect.

	def _distance_to_circle(self, other_circle: Hitbox) -> float:
		"""
		Returns the distance between this circle's boundaries and another circle's boundaries.
		:param other_circle: The other circle hitbox.
		:return: The distance between the boundaries of the two circles.
		"""
		return math.sqrt((self.center.x - other_circle.center.x) ** 2 + (self.center.y - other_circle.center.y) ** 2) - self.radius - other_circle.radius

	# TODO this can be a Hitbox method... it just finds the x and y distances between the hitboxes' bounding rects.
	# TODO however, there is still some distance required for circle hitboxes. Figure this out.
	def xy_distance_to_rect(self, other_rect: Hitbox) -> tuple[float, float]:
		# in_x_range = (rect.left_x < this.center.x < rect.right_x)
		# in_y_range = (rect.top_y < this.center.y < rect.bottom_y)
		# if in_x_range and in_y_range:
		# 	distance = 0
		# elif in_x_range and not in_y_range:
		# 	distance = max min bull
		# elif in_y_range and not in_x_range:
		#	distance = ditto bull
		# else:
		#	distance = slope bull
		# return distance

		x_distance = abs(other_rect.center.x - self.center.x) - (other_rect.dimensions.x / 2) - self.radius
		y_distance = abs(other_rect.center.y - self.center.y) - (other_rect.dimensions.y / 2) - self.radius
		return x_distance, y_distance
