from scene import Scene
from random import randint

class Death(Scene):

  quips = [
    "You died. You kinda suck at this.",
    "Your mom would be proud... if she were smarter",
    "Such a looser...",
    "I have a small puppy that's better at this"
  ]

  def enter(self):
    print Death.quips[randint(0, len(self.quips)-1)]
    exit(1)