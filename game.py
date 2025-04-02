import arcade
from levels import GameLevel

# Screen dimensions and title.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "SHS Game: Intro to Electrical Circuits"

FRAME_WIDTH = 16
FRAME_HEIGHT = 32
FRAMES_PER_DIRECTION = 4

DOWN = 0
LEFT = 1
RIGHT = 2
UP = 3

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player_sprite = None
        self.all_sprites = None
        self.current_level = None
        self.level_number = 1
        self.walk_textures = {
            DOWN: [],
            LEFT: [],
            RIGHT: [],
            UP: []
        }
        self.current_frame = 0
        self.current_direction = DOWN  # default direction

    def setup(self):
        self.all_sprites = arcade.SpriteList()
        sprite_sheet = arcade.load_spritesheet("resources/player.png")
        
        all_textures = sprite_sheet.get_texture_grid(
            size=(FRAME_WIDTH, FRAME_HEIGHT),
            columns=FRAMES_PER_DIRECTION,
            count=16
        )

        # see player.png for direction sorting
        self.walk_textures[DOWN] = all_textures[0:4]
        self.walk_textures[RIGHT] = all_textures[4:8]
        self.walk_textures[UP] = all_textures[8:12]
        self.walk_textures[LEFT] = all_textures[12:16]

        self.player_sprite = arcade.Sprite()
        self.player_sprite.scale = 2.0  # increase sprite size by 2 
        self.player_sprite.textures = self.walk_textures[DOWN]
        self.player_sprite.texture = self.walk_textures[DOWN][0]
        self.player_sprite.center_x = SCREEN_WIDTH // 2
        self.player_sprite.center_y = SCREEN_HEIGHT // 2
        self.all_sprites.append(self.player_sprite)

        self.setup_level(self.level_number)

    def setup_level(self, level_number):
        self.current_level = GameLevel(level_number)
        self.current_level.setup()

    def on_draw(self):
        self.clear()
        if self.current_level:
            self.current_level.draw()
        self.all_sprites.draw()

    def on_update(self, delta_time):
        self.all_sprites.update()
        
        # only update direction if moving
        if self.player_sprite.change_x != 0 or self.player_sprite.change_y != 0:
            self.current_frame = (self.current_frame + 1) % FRAMES_PER_DIRECTION
            self.player_sprite.texture = self.walk_textures[self.current_direction][self.current_frame]
        else:
            self.player_sprite.texture = self.walk_textures[self.current_direction][0]

        if self.current_level:
            self.current_level.update(delta_time)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
            self.current_direction = LEFT
            self.player_sprite.textures = self.walk_textures[LEFT]
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5
            self.current_direction = RIGHT
            self.player_sprite.textures = self.walk_textures[RIGHT]
        elif key == arcade.key.UP:
            self.player_sprite.change_y = 5
            self.current_direction = UP
            self.player_sprite.textures = self.walk_textures[UP]
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -5
            self.current_direction = DOWN
            self.player_sprite.textures = self.walk_textures[DOWN]

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player_sprite.change_x = 0
        if key in (arcade.key.UP, arcade.key.DOWN):
            self.player_sprite.change_y = 0
