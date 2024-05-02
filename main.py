import arcade
import random
from game_state import GameState

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
DEFAULT_LINE_HEIGHT = 45

class personnage:

    def __init__(self):
        self.hp = 0
        self.weapon = 0
        self.armor = 0

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        arcade.set_background_color(arcade.color.BLACK_OLIVE)
        self.game_state = GameState.NOT_STARTED
        self.playerV = personnage()
        self.ennemyV = personnage()
        self.player()
        self.ennemy()

    def player(self):
        self.playerV.hp = 20
        self.playerV.weapon = 5
        self.playerV.armor = 3


    def ennemy(self):
        self.ennemyV.hp = 40
        self.ennemyV.weapon = 10
        self.ennemyV.armor = 1

    def attack(self):
        self.choice1 = arcade.draw_text("attack", 250, 210, arcade.color.AO, 50, 10)
        self.choice1

    def prepare(self):
        pass

    def setup(self):
        if self.game_state == GameState.NOT_STARTED:
            arcade.draw_text("HELLO!",
                            0,
                            SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 2,
                            arcade.color.PURPLE,
                            60,
                            width=SCREEN_WIDTH,
                            align="center")
        arcade.draw_rectangle_outline(380, 230, 500, 100, arcade.color.DARK_RED, 5, 0)
        arcade.draw_text("prepare", 770, 210, arcade.color.AO, 50, 10)
        arcade.draw_rectangle_outline(900, 230, 500, 100, arcade.color.DARK_RED, 5, 0)
        self.attack()
        arcade.draw_rectangle_outline(380, 110, 500, 100, arcade.color.DARK_RED, 5, 0)
        arcade.draw_rectangle_outline(900, 110, 500, 100, arcade.color.DARK_RED, 5, 0)


    def on_draw(self):
        arcade.start_render()
        self.setup()
        self.player()



    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            if self.game_state == GameState.NOT_STARTED:
               self.game_state = GameState.ROUND_ACTIVE
            elif self.game_state == GameState.ROUND_ACTIVE:
                self.game_state = GameState.ROUND_DONE
            elif self.game_state == GameState.GAME_OVER:
                self.game_state = GameState.ROUND_ACTIVE

    def on_mouse_press(self, x, y, button, key_modifiers):

        if self.choice1.collides_with_point((x, y)):
            print("lol")


def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()
main()

