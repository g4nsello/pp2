import pygame
from datetime import datetime
pygame.init()
screen = pygame.display.set_mode((829, 836))
done = False
bg_image = pygame.image.load(r'C:\Users\hhhg4\Desktop\pp2\lab07\images\body.png')
sec_img = pygame.image.load(r'C:\Users\hhhg4\Desktop\pp2\lab07\images\hand1.png')
min_img = pygame.image.load(r'C:\Users\hhhg4\Desktop\pp2\lab07\images\hand2.png')
rect = bg_image.get_rect(center=(415, 418))

while not done:
    screen.blit(bg_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    time = datetime.now().time()

    sec_angle = (time.second * 60)
    nsec_img = pygame.transform.rotate(sec_img, sec_angle)
    sec_rect = nsec_img.get_rect(center=rect.center)
    screen.blit(nsec_img, sec_rect.topleft)

    min_angle = (time.minute * 60)
    nmin_img = pygame.transform.rotate(min_img, min_angle)
    min_rect = nmin_img.get_rect(center=rect.center)
    screen.blit(nmin_img, min_rect.topleft)

    pygame.display.flip()