import arcade
import random

BREIDD = 640
HAED = 480
NAFN_LEIKS = "Skotleikurinn"

class Leikmadur(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")

class Skot(arcade.Sprite):
    def __init__(self, geimskip):
        super().__init__(":resources:images/space_shooter/laserBlue01.png")

class Ovinur(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")

class Leikurinn(arcade.Window):
    def __init__(self, breidd, haed, nafn_leiksins):
        super().__init__(breidd, haed, nafn_leiksins)
        self.bakgrunnur = arcade.load_texture(":resources:images/backgrounds/stars.png")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, BREIDD, HAED, self.bakgrunnur)

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def update(self, delta_time):
        pass



leikur = Leikurinn(BREIDD, HAED, NAFN_LEIKS)
arcade.run()
