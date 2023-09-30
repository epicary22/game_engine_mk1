import pygame as pg
from hitbox.hitbox import Hitbox
from hitbox.circle_hitbox import CircleHitbox

h = Hitbox(pg.Vector2(40.5, 30.5), None, center=pg.Vector2(100.03, 200.77), rounding=False)
g = Hitbox(pg.Vector2(40.5, 30.5), None, center=pg.Vector2(100.03, 200.77), rounding=True)

c = CircleHitbox(10, pg.Vector2(0, 0), rounding=True)
d = CircleHitbox(10, pg.Vector2(19, 0), rounding=True)
print(c.distance_to(d))
