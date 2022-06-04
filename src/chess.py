from unittest import runner
import pygame as p 
from eng import GameState;

import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__))))

class Chess:
    def __init__(self) -> None:
        self.width = self.height = 512
        self.scale = 8
        self.sq_size = self.height // self.scale
        self.max_fps = 15
        self.images = {}

    def load_images(self):
        piece_labels = ['P','N','B','R','Q','K']
        for piece in piece_labels:
            wp = f'w{piece}'
            bp = f'b{piece}'
            self.images[wp] = p.transform.scale(p.image.load(rf"img\{wp}.png"), (self.sq_size, self.sq_size))
            self.images[bp] = p.transform.scale(p.image.load(rf"img\{bp}.png"), (self.sq_size, self.sq_size))
    
    def main(self):
        p.init()
        screen = p.display.set_mode((self.width, self.height))
        clk = p.time.Clock()
        screen.fill(p.Color('white'))

        gs = GameState()
        self.load_images()
        
        running = True
        while running:
            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False

                self.update_gs(screen, gs)
                clk.tick(self.max_fps)
                p.display.flip()


    def update_gs(self, screen, gs):
        self.update_board(screen)
        self.update_pieces(screen, gs.board)
        

    def update_board(self, screen):
        colors = [p.Color(214, 193, 161), p.Color(147, 111, 81)]
        for r in range(self.scale):
            for c in range(self.scale):
                color = colors[(r + c) % 2]
                p.draw.rect(screen, color, p.Rect(c * self.sq_size, r * self.sq_size, self.sq_size, self.sq_size))

    def update_pieces(self, screen, board):
        for r in range(self.scale):
            for c in range(self.scale):
                piece = board[r][c]
                if piece:
                    screen.blit(self.images[piece], (c * self.sq_size, r * self.sq_size))
                    
if __name__ == '__main__':
    Chess().main()