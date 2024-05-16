import arcade

class HealthBar:
    def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp

    def draw(self):

        ratio = self.hp / self.max_hp
        arcade.draw_xywh_rectangle_filled(self.x, self.y, self.w, self.h, arcade.color.RED)
        arcade.draw_xywh_rectangle_filled(self.x, self.y, self.w * ratio, self.h, arcade.color.GREEN)
        #print(ratio)RED, 10, 0)