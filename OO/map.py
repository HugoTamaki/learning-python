from central_corridor import CentralCorridor
from laser_weapon_armory import LaserWeaponArmory
from the_bridge import TheBridge
from escape_pod import EscapePod
from death import Death

class Map(object):

  scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death()
  }

  def __init__(self, start_scene):
    self.start_scene = start_scene

  def next_scene(self, scene_name):
    return Map.scenes[scene_name]

  def opening_scene(self):
    return self.next_scene(self.start_scene)