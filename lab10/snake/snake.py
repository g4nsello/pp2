import pygame
import time
import random
import psycopg2

# Function to initialize database connection
def initialize_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="arsen060708"
        )
        cur = conn.cursor()
        return conn, cur
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)

# Function to create user and user_score columns if not exists
def create_user_table(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS snake_scores (id SERIAL PRIMARY KEY, username VARCHAR(50) UNIQUE, user_score INTEGER)")

# Function to insert or update user score
def update_user_score(cur, conn, username, score):
    cur.execute("SELECT * FROM snake_scores WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        # Update user's score if user exists
        cur.execute("UPDATE snake_scores SET user_score = %s WHERE username = %s", (score, username))
    else:
        # Insert new user with score if user doesn't exist
        cur.execute("INSERT INTO snake_scores (username, user_score) VALUES (%s, %s)", (username, score))
    conn.commit()

# Function to get user's current level based on their score


# Function to display current user level
def show_user_level(username, cur):
    cur.execute("SELECT user_score FROM snake_scores WHERE username = %s", (username,))
    user_score = cur.fetchone()
    score=user_score[0]
    if user_score:
        print(f"Welcome back, {username}! Your current level is {user_score[0]}.")
    else:
        print(f"Welcome, {username}! You are a new player.")

# Initialize database connection and cursor
conn, cur = initialize_db()
create_user_table(cur)

# Get user's username
username = input("Enter your username: ")

# Display user's current level
show_user_level(username, cur)

# Snake game initialization
snake_speed = 15
window_x = 700
window_y = 700
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
pygame.init()
pygame.display.set_caption('Snakes')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()
snake_position = [100, 50]
snake_body = [[100, 50]]
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                random.randrange(1, (window_y//10)) * 10]
def show_score(choice, color, font, size):

	# creating font object score_font
	score_font = pygame.font.SysFont(font, size)
	
	# create the display surface object 
	# score_surface
	score_surface = score_font.render('Score : ' + str(score), True, color)
	
	# create a rectangular object for the text
	# surface object
	score_rect = score_surface.get_rect()
	
	# displaying text
	game_window.blit(score_surface, score_rect)
fruit_spawn = True
direction = 'RIGHT'
change_to = direction
def level(username, cur):
    cur.execute("SELECT user_score FROM snake_scores WHERE username = %s", (username,))
    user_score = cur.fetchone()
    l= user_score[0]
    return l
score=level(username, cur)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    d=5
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        if score <=20:
            d=10
        if score<=50 and score >20:
            d=15
        if score<=80 and score >50:
            d=20
        fruit_spawn = False
    else:
        snake_body.pop()
        
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                        random.randrange(1, (window_y//10)) * 10]
        
    fruit_spawn = True
    game_window.fill(black)
    show_score(1, white, 'times new roman', 20)
    for pos in snake_body:
        pygame.draw.rect(game_window, red, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        update_user_score(cur, conn, username, score)
        print("Game Over! Your final score is:", score)
        pygame.quit()
        quit()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        update_user_score(cur, conn, username, score)
        print("Game Over! Your final score is:", score)
        pygame.quit()
        quit()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            update_user_score(cur, conn, username, score)
            print("Game Over! Your final score is:", score)
            pygame.quit()
            quit()

    pygame.display.update()
    fps.tick(snake_speed)
