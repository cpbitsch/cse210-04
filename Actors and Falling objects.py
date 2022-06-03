from game.casting.actor import Actor 
from game.casting.artifact import Artifact  
from game.shared.color import Color                             
from game.shared.point import Point

FRAME_RATE = 22
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = random.randint(1,3) #like in the director.py, the number of the primitive artifacts created
cast = Cast()

texts = ["W", "*"]
for n in range(DEFAULT_ARTIFACTS):
        text = random.choice(texts)
        x = random.randint(1, MAX_X)
        y = 0
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(25)
        artifact.set_color(color)
        artifact.set_position(position)
        cast.add_actor("artifacts", artifact)