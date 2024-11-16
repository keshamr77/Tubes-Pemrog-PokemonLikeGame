from settings import *
from pytmx.util_pygame import load_pygame
from os.path import join, dirname, abspath

from sprites import Sprite, AnimatedSprite
from entities import Player
from groups import AllSprites

from support import *

class Game:
    def __init__(self) :
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Hunt for Ambalabu')
        self.clock = pygame.time.Clock()

        # Groups
        self.all_sprites = AllSprites()

        self.import_assets()
        self.setup(self.tmx_maps['world'], 'house')
        
    def import_assets(self) :
        base_path = dirname(dirname(abspath(__file__)))
        map_path = join(base_path, "data", "maps", "world.tmx")
        hospital_path =  join(base_path, "data", "maps", "hospital.tmx")
        water_path = join(base_path, "graphics", "tilesets", "water")
        coast_path = join(base_path, "graphics", "tilesets", "coast")
        self.tmx_maps = {
            'world': load_pygame(map_path), 
            'hospital' : load_pygame(hospital_path)
                       }
        
        self.overworld_frames = {
            'water' : import_folder(water_path),
            'coast' : coast_importer(24,12, coast_path)
        }

    def setup(self, tmx_map, player_start_pos):
        # Terrain
        for layer in ['Terrain', 'Terrain Top'] :
            for x,y, surf in tmx_map.get_layer_by_name('Terrain').tiles() :
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        
        
        # Entities
        for obj in tmx_map.get_layer_by_name('Entities') :
            if obj.name == 'Player' and obj.properties['pos'] == player_start_pos:
                self.player = Player((obj.x, obj.y), self.all_sprites)
        
        # Objects
        for obj in tmx_map.get_layer_by_name('Objects') :
            Sprite((obj.x, obj.y), obj.image, self.all_sprites)
        
        # Water 
        for obj in tmx_map.get_layer_by_name('Water') :
            for x in range(int(obj.x), int(obj.x + obj.width), TILE_SIZE) : 
                for y in range(int(obj.y), int(obj.y + obj.height), TILE_SIZE) :
                    AnimatedSprite((x,y), self.overworld_frames['water'], self.all_sprites)
                
    def run(self) :
        while True :
            dt = self.clock.tick() / 1000
            #Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            #Game Logic
            self.all_sprites.update(dt)
            self.display_surface.fill('black')
            self.all_sprites.draw(self.player.rect.center)
            print(self.clock.get_fps())

            pygame.display.update()

if __name__ == '__main__' :
    game = Game()
    game.run()
