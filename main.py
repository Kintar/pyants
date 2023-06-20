import pygame
from pygame import Vector2

from ant import Ant


class App:
    def __init__(self):
        self.running = True
        self.display_surf = None
        self.size = self.weight, self.height = 800, 600
        ant = Ant()
        ant.position = Vector2(400, 300)
        ant.direction = Vector2(0, 1)
        self.ant = ant
        self.ticks_last_frame = 0

    def on_init(self):
        pygame.init()
        pygame.display.set_caption("PyAnts!")
        self.display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def on_update(self):
        t = pygame.time.get_ticks()
        delta = (t - self.ticks_last_frame) / 1000.0
        self.ticks_last_frame = t
        self.ant.on_update(delta)
        pygame.display.flip()

    def on_render(self):
        self.ant.on_render(self.display_surf)

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self.running = False
            print("on_init failed")

        print("running...")
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_update()
            self.on_render()

        print("exited")
        self.on_cleanup()


if __name__ == "__main__":
    app = App()
    app.on_execute()
else:
    print(__name__)
