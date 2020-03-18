import pygame
import random
import numpy as np
import matplotlib.pyplot as plt
from blob import Blob


WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])

class Simulation():
    
    def __init__(self,population,interaction,init_affected):
        self.population = population
        self.interaction = interaction
        self.init_affected = init_affected
        self.clock = pygame.time.Clock()
        self.infected = [500,501,502]

    def detect_colition(self,blobs):
        
        for blob_id in blobs:
            blob = blobs[blob_id]

            # find a way to detect a collition 
            self.infected.append(random.randint(200,500))

            return blobs 
        
        
    def draw(self,blobs):
        screen.fill(WHITE)
        blobs = self.detect_colition(blobs)
        for blob_id in blobs:
            blob = blobs[blob_id]
            if blob_id in self.infected:
                blob.color = RED
                pygame.draw.circle(screen,blob.color,[blob.x,blob.y],blob.size)
            else:
                pygame.draw.circle(screen,blob.color,[blob.x,blob.y],blob.size)
            blob.move()
            #detect collition hear
        pygame.display.update()

    def render(self):
        
        blobs = dict(enumerate([Blob(GREEN) for i in range(self.population)]))

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            self.draw(blobs)

    
def main():
    sim = Simulation(1000,23,3)
    sim.render()


if __name__ == "__main__":
    main()

