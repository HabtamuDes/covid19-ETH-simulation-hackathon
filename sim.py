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
        self.infected = [500]

    def detect_collision(self,blobs):
        
        for blob_id in blobs:
            blob = blobs[blob_id]

            for i in self.infected:
                inf = blobs[i]
                #equlidian distance  
                #dis = (x1-x0)**2 + (y1-y0)**2

                distance = np.sqrt((blob.x - inf.x)**2 + (blob.y - inf.y)**2)
                
                if distance <15 and blob_id not in self.infected:
                    print([distance,blob_id])
                    self.infected.append(blob_id)
                    
        
        
    def draw(self,blobs):
        screen.fill(WHITE)
        self.detect_collision(blobs)
        for blob_id in blobs:
            blob = blobs[blob_id]
            if blob_id in self.infected:
                blob.color = RED
                pygame.draw.circle(screen,blob.color,[blob.x,blob.y],blob.size)
            else:
                pygame.draw.circle(screen,blob.color,[blob.x,blob.y],blob.size)
            blob.move()
        pygame.display.update()

    def render(self):
        
        #id and object
        blobs = dict(enumerate([Blob(GREEN) for i in range(self.population)]))

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            self.draw(blobs)

        pygame.quit()

    
def main():
    sim = Simulation(1000,23,3)
    sim.render()


if __name__ == "__main__":
    main()

