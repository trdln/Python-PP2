import pygame
all = pygame.font.get_fonts()
out = open("all.txt",'a')
out.writelines(all)
print(all)