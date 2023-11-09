import pygame
import time
import random
# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 初始化游戏
pygame.init()

# 设置游戏窗口大小
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇")

# 设置游戏时间和速度
clock = pygame.time.Clock()
snake_speed = 15

# 设置蛇的初始位置和速度
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = "RIGHT"
change_to = direction

# 设置食物的初始位置
food_position = [random.randrange(1, (width // 10)) * 10,
                 random.randrange(1, (height // 10)) * 10]
food_spawn = True

# 游戏循环
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    # 好像需要这么一个防止乱按的东西确保蛇不会乱跑来着
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    # 方向键操作后蛇的位置更新
    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] += 10
    if direction == "LEFT":
        snake_position[0] -= 10
    if direction == "RIGHT":
        snake_position[0] += 10

    # 蛇吃食物后长大
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        food_spawn = False
    else:
        snake_body.pop()

    # 每吃掉一个出现一个新的食物
    if not food_spawn:
        food_position = [random.randrange(1, (width // 10)) * 10,
                         random.randrange(1, (height // 10)) * 10]
    food_spawn = True

    # 绘制游戏窗口
    window.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(window, GREEN, pygame.Rect(
            pos[0], pos[1], 10, 10))

    pygame.draw.rect(window, RED, pygame.Rect(
        food_position[0], food_position[1], 10, 10))

    pygame.display.flip()

    # gameover的条件
    if snake_position[0] < 0 or snake_position[0] > width - 10 or snake_position[1] < 0 or snake_position[
        1] > height - 10:
        game_over = True
    if snake_position in snake_body[1:]:
        game_over = True

    # 会闪退加一个控制游戏速度
    clock.tick(snake_speed)

# 退出
pygame.quit()