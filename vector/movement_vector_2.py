import pygame as pg


class MovementVector2:
	"""
	A positionless vector used to describe the movement of an obejct.
	"""
	def __init__(self, framerate: float, initial_velocity: pg.Vector2 = None, initial_acceleration: pg.Vector2 = None):
		"""
		Creates a positionless vector to describe the movement of an object.
		:param framerate: The framerate of the surrounding application.
		:param initial_velocity: The initial velocity of the vector, in pixels per frame.
		:param initial_acceleration: The initial acceleration of the vector, in pixels per frame.
		"""
		self.framerate = framerate
		if initial_velocity is not None:
			self.velocity = initial_velocity
		else:
			self.velocity = pg.Vector2(0, 0)
		if initial_acceleration is not None:
			self.acceleration = initial_acceleration
		else:
			self.acceleration = pg.Vector2(0, 0)
		
	def _frames_passed(self, dt: float):
		"""
		Calculates the number of frames passed given an amount of time.
		:param dt: The amount of time passed.
		:return: The amount of frames passed.
		"""
		return dt * self.framerate
		
	def step(self, position_vector: pg.Vector2, dt: float):
		"""
		Moves a position vector by an amount determined by dt. Returns a new position vector object. Does not affect
		the original position vector object.
		:param position_vector: A 2D position vector.
		:param dt: The amount of time passed.
		:return: The original position vector.
		"""
		new_position_vector = pg.Vector2(position_vector.xy)
		frames = self._frames_passed(dt)
		new_position_vector.x += self.velocity.x * frames
		new_position_vector.y += self.velocity.y * frames
		return new_position_vector
		
	def step_ip(self, position_vector: pg.Vector2, dt: float):
		"""
		Moves a position vector by an amount determined by dt. Affects and returns the original position vector object.
		:param position_vector: A 2D position vector.
		:param dt: The amount of time passed.
		:return: The original position vector.
		"""
		frames = self._frames_passed(dt)
		position_vector.x += self.velocity.x * frames
		position_vector.y += self.velocity.y * frames
		return position_vector
	
	def accelerate(self, dt: float):
		"""
		Adds the acceleration of this vector to its current velocity. Affects and returns the original vector.
		:param dt: The amount of time passed.
		:return: The original movement vector.
		"""
		frames = self._frames_passed(dt)
		self.velocity.x += self.acceleration.x * frames
		self.velocity.y += self.acceleration.y * frames
		return self
	
	def accelerate_ip(self, dt: float):
		"""
		Adds the acceleration of this vector to its current velocity. Returns a new vector. Does not affect the original
		vector.
		:param dt: The amount of time passed.
		:return: A new movement vector.
		"""
		new_movement_vector = MovementVector2(self.framerate, self.velocity, self.acceleration)
		frames = self._frames_passed(dt)
		new_movement_vector.velocity.x += new_movement_vector.acceleration.x * frames
		new_movement_vector.velocity.y += new_movement_vector.acceleration.y * frames
		return new_movement_vector

	# TODO add more vector-y methods
	
