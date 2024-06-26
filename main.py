import arcade
import random
from game_state import GameState
from health_bar import HealthBar

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
DEFAULT_LINE_HEIGHT = 45


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        arcade.set_background_color(arcade.color.BLACK_OLIVE)
        self.game_state = GameState.NOT_STARTED
        #self.player()
        #self.ennemy()
        self.playerV = HealthBar(30, 500, 250, 50, 120)
        self.ennemyV = HealthBar(1000, 500, 250, 50, 100)
        self.player()
        self.ennemy()
        self.player_choice = 0
        self.ennemy_choice = 0

        #self.health_bar = HealthBar(30, 500, 250, 50, 100)

    def player(self):
        self.playerV.max_hp = 120
        self.playerV.weapon = 10
        self.playerV.armor = 3
        arcade.draw_text("player",
                         30,
                         SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT *3,
                         arcade.color.WHITE_SMOKE,
                         45,
                         width=SCREEN_WIDTH,
                         align="left")
        self.playerV.draw()


    def ennemy(self):
        self.ennemyV.max_hp = 100
        self.ennemyV.weapon = 15
        self.ennemyV.armor = 1
        arcade.draw_text("ennemy",
                         1035 ,
                         SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 3,
                         arcade.color.WHITE_SMOKE,
                         45,
                         width=SCREEN_WIDTH,
                         align="left")
        self.ennemyV.draw()

        if self.game_state == GameState.ROUND_ENNEMY:
            if self.player_choice == 1:
                R = random.randint(1,2)
                if R == 1:
                    self.ennemy_choice = 1
                else:
                    self.ennemy_choice = 2
            else:
                self.ennemy_choice = 1



    def attack(self):
        self.choice1 = arcade.create_text_sprite("attack", 250, 210, arcade.color.AO, 50)
        self.choice1.draw()


    def prepare(self):
        self.choice2 = arcade.create_text_sprite("prepare", 770, 210, arcade.color.AO, 50)
        self.choice2.draw()

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
        arcade.draw_rectangle_outline(900, 230, 500, 100, arcade.color.DARK_RED, 5, 0)
        self.attack()
        self.prepare()
        arcade.draw_rectangle_outline(380, 110, 500, 100, arcade.color.DARK_RED, 5, 0)
        arcade.draw_rectangle_outline(900, 110, 500, 100, arcade.color.DARK_RED, 5, 0)




    def on_draw(self,):
        arcade.start_render()
        self.setup()
        self.player()
        self.ennemy()
        #self.health_bar.draw()



    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            if self.game_state == GameState.NOT_STARTED:
               self.game_state = GameState.ROUND_PLAYER
            #elif self.game_state == GameState.ROUND_PLAYER:
                #self.game_state = GameState.ROUND_ENNEMY
            #elif self.game_state == GameState.ROUND_ENNEMY:
                #self.game_state = GameState.GAME_OVER
            #elif self.game_state == GameState.GAME_OVER:
                #self.game_state = GameState.ROUND_PLAYER

    def on_mouse_press(self, x, y, button, key_modifiers):

        if self.choice1.collides_with_point((x, y)):
            #print("attack")
            #print(self.ennemyV.hp)
            self.ennemyV.hp -= self.playerV.weapon - self.ennemyV.armor
            self.player_choice = 1
        elif self.choice2.collides_with_point((x, y)):
            #print("prepare")
            self.ennemy_choice = 2
        self.game_state = GameState.ROUND_ENNEMY



def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()
main()

