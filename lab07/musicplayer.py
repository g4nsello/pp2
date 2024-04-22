import pygame

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((800, 700))
done = False
songs = [r'C:\Users\hhhg4\Desktop\pp2\lab07\phonk\p1.mp3',
         r'C:\Users\hhhg4\Desktop\pp2\lab07\phonk\p2.mp3',
         r'C:\Users\hhhg4\Desktop\pp2\lab07\phonk\p3.mp3',]
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
i = 0
a = True
bg = pygame.image.load(r'C:\Users\hhhg4\Desktop\pp2\lab07\images\cat.jpg')
screen.blit(bg, (0, 0))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                i = (i + 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                i = (i - 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
            elif event.key == pygame.K_SPACE:
                if a:
                    pygame.mixer.music.stop()
                    a = False
                else:
                    pygame.mixer.music.play()
                    a = True

    pygame.display.flip()