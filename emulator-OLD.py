import pygame
import importlib
from time import time
pygame.init()
CLOCK_SPEED = 1/60
class Cpx:
    def __init__(self,file):
        self.file = open(f"{file}.py")
        self.pixels = []
        self.raw =self.file.readlines()
        self.vars= []
        self.varnames = []
        self.imports = []
        self.instructions = [("math",round,(1.5,1))]
        pygame.display.set_mode((600,600))
        self.surface = pygame.display.get_surface()
        self.read_file()
        self.parse_instructions()
        self.loop()
    def read_file(self):
        for c in range(len(self.raw)-1):
              self.raw[c] = self.raw[c][:-1]
    def parse_instructions(self):
        for c in range(len(self.raw)):
            if True:
                pass
    def render(self):
        self.surface.fill((255,255,255))
        pygame.display.flip()
    def execute(self,mod,mea,arg):
        module = mod
        for c in range(len(self.instructions)):
            module.self.instruciotns[0].self.instructions[1].self.instructions[2]
    def loop(self):
        global CLOCK_SPEED
        time1 = time()
        time2 = time()
        while True:
            if (time1 - time2) >= CLOCK_SPEED:
                self.render()
                time1 = time2
            time2 = time()
Cpx("test")
