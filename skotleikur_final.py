import arcade
import random

BREIDD = 640
HAED = 480
NAFN_LEIKS = "Skotleikurinn"
SKALI = 0.75
HRADI_SKOTA = 10

class Leikmadur(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = BREIDD / 2
        self.center_y = HAED / 8
        self.scale = SKALI

class Skot(arcade.Sprite):
    def __init__(self, geimskip):
        super().__init__(":resources:images/space_shooter/laserBlue01.png")
        self.angle = 90
        self.center_x = geimskip.center_x
        self.bottom = geimskip.top

class Ovinur(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = random.randint(20, BREIDD - 20) #BREIDD / 2
        self.center_y = HAED + 50
        self.scale = SKALI * 0.75
        self.angle = 180

class Leikurinn(arcade.Window):
    def __init__(self, breidd, haed, nafn_leiksins):
        super().__init__(breidd, haed, nafn_leiksins)
        self.bakgrunnur = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.geimskip = Leikmadur()
        self.oll_skot = arcade.SpriteList()
        self.ovinir = arcade.SpriteList()
        self.stig = 0
        for i in range(10):
            self.ovinir.append(Ovinur())

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, BREIDD, HAED, self.bakgrunnur)
        self.geimskip.draw()
        self.oll_skot.draw()
        self.ovinir.draw()
        arcade.draw_text(f"Stig: {self.stig}", 10, 20, arcade.color.WHITE, 14)


    def on_mouse_motion(self, x, y, dx, dy):
        self.geimskip.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        skot = Skot(self.geimskip)
        self.oll_skot.append(skot)

    def update(self, delta_time):
        self.geimskip.update()
        self.oll_skot.update()
        self.ovinir.update()

        for ovinur in self.ovinir:
            if ovinur.center_y > HAED - HAED / 8:
                ovinur.center_y -= 1

        for skot in self.oll_skot:
            
            skot.center_y += HRADI_SKOTA

            skot_hitti = arcade.check_for_collision_with_list(skot, self.ovinir)

            for ovinur in skot_hitti:
                self.stig += 1
                ovinur.remove_from_sprite_lists()

            if skot.bottom > HAED:
                skot.remove_from_sprite_lists()
        
        if len(self.ovinir) < 5:
            self.ovinir.append(Ovinur())



leikur = Leikurinn(BREIDD, HAED, NAFN_LEIKS)
arcade.run()
