import pygame as pg
from hitbox.hitbox import Hitbox

h = Hitbox(pg.Vector2(40.5, 30.5), None, center=pg.Vector2(100.03, 200.77), rounding=False)
g = Hitbox(pg.Vector2(40.5, 30.5), None, center=pg.Vector2(100.03, 200.77), rounding=True)
