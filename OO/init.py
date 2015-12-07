from sys import exit
from scene import *
from engine import *
from death import *
from central_corridor import *
from escape_pod import *
from laser_weapon_armory import *
from the_bridge import *
from map import *

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
