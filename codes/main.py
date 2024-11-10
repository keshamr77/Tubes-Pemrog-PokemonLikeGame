from settings import *
from pytmx.util_pygame import load_pygame
from os.path import join

class Game:
    def __init__(self) :
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Hunt for Ambalabu')

        self.import_assets()
        self.setup(self.tmx_maps['world'], 'house')
        
    def import_assets(self) :
        self.tmx_maps = {'world' : load_pygame('/data/maps/world.tmx')}
 
    def setup(self, tmx_map, player_start_pos):
        for x,y, surf in tmx_map.get_layer_by_name('Terrain') :
            print(x,y,surf)
    
    def run(self) :
        while True :
            #Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            #Game Logic
            pygame.display.update()

if __name__ == '__main__' :
    game = Game()
    game.run()
