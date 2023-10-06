import pygame as pg
from hitbox.hitbox import Hitbox
from hitbox.circle_hitbox import CircleHitbox
from vector.movement_vector_2 import MovementVector2

h = Hitbox(pg.Vector2(40.5, 30.5), None, center=pg.Vector2(100.03, 200.77), rounding=False)
g = Hitbox(pg.Vector2(40.5, 30.5), None, center=pg.Vector2(100.03, 200.77), rounding=True)

c = CircleHitbox(10, pg.Vector2(0, 0), rounding=True)
d = CircleHitbox(10, pg.Vector2(19, 0), rounding=True)
print(c.distance_to(d))

m = MovementVector2(60, pg.Vector2(10, 10), pg.Vector2(-0.001, -0.002))
for _ in range(100):
	m.accelerate_ip(1/60)
	print(m.velocity.xy)

