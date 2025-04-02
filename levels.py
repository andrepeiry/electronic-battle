import arcade

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

class TileMap:
    def __init__(self, map_data, tile_size, tile_image):
        self.map_data = map_data
        self.tile_size = tile_size
        self.tile_image = tile_image
        self.tile_list = arcade.SpriteList()

    def setup(self):
        for row_index, row in enumerate(self.map_data):
            for col_index, cell in enumerate(row):
                if cell == "W":
                    tile_sprite = arcade.Sprite(self.tile_image, scale=1.0)
                    # Tint wall tiles to differentiate them.
                    tile_sprite.color = arcade.color.GRAY
                elif cell == ".":
                    tile_sprite = arcade.Sprite(self.tile_image, scale=1.0)
                else:
                    continue
                tile_sprite.center_x = WINDOW_WIDTH / 2
                tile_sprite.center_y = WINDOW_HEIGHT / 2
                self.tile_list.append(tile_sprite)

    def draw(self):
        self.tile_list.draw()

class GameLevel:
    def __init__(self, level_number):
        self.level_number = level_number
        self.instructions = ""
        self.circuit_elements = []
        self.enemies = []
        self.tile_map = None

    def setup(self):
        if self.level_number == 1:
            self.instructions = "Level 1: Select the correct resistor value to pass the current meter reading!" # Or something like this. 
        elif self.level_number == 2:
            self.instructions = "Level 2: Use the capacitor sword and observe how the capacitor behaves when full."

        # room with walls ("W") around and floor (".") in the middle (very basic for now)
        map_data = [
            "WWWWWWWWWW",
            "W........W",
            "W........W",
            "W........W",
            "WWWWWWWWWW"
        ]
        tile_size = 32
        tile_image = "/Users/Zachary/Desktop/BA6/SHS_Video_Game/resources/lvl_background.png"
        self.tile_map = TileMap(map_data, tile_size, tile_image)
        self.tile_map.setup()

    def update(self, delta_time):
        #TODO: Update lvl logic (e.g. check circuit conditions etc...)
        pass

    def draw(self):
        if self.tile_map:
            self.tile_map.draw()
        # level instructions
        arcade.draw_text(
            self.instructions,
            20,
            580,
            arcade.color.WHITE,
            20
        )
