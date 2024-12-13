import pygame
import time
import random


def Snake_game():
    snake_speed = 15

    # Размер окна
    window_x = 720
    window_y = 480

    # Определяем цвета
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)

    # Инициализируем Pygame
    pygame.init()

    # Инициализируем игровое окно
    pygame.display.set_caption("Змейка")
    game_window = pygame.display.set_mode((window_x, window_y))

    # FPS (frames per second) контроллер
    fps = pygame.time.Clock()

    # Определяем позицию по умолчанию для змейки
    snake_position = [100, 50]

    # Определяем первые 4 блока змейки
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    # Позиция яблока
    fruit_position = [
        random.randrange(1, (window_x // 10)) * 10,
        random.randrange(1, (window_y // 10)) * 10,
    ]

    fruit_spawn = True

    # Змейка по уцмолчанию двигается вправо
    direction = "RIGHT"
    change_to = direction

    # Количество набранных очков
    score = 0

    # Функция для отображения счёта
    def show_score(choice, color, font, size):

        # Создание объекта score_font
        score_font = pygame.font.SysFont(font, size)

        score_surface = score_font.render("Счёт : " + str(score), True, color)

        # Создание четырёхугольника для счёта
        score_rect = score_surface.get_rect()

        # отображаем текст
        game_window.blit(score_surface, score_rect)

    # Функция конца игры
    def game_over():

        try:
            with open("highscore.txt", "r") as f:
                current_highscore = int(f.read())
        except (FileNotFoundError, ValueError):
            current_highscore = 0  # Значение счёта по умолчанию

            # Сравнение нынешнего результата с максимальным
        if score > current_highscore:
            # Если нынешний результат больше, чем максимальный, то записываем нынешний результат в файл
            with open("highscore.txt", "w") as f:
                f.write("%d" % score)

        my_font = pygame.font.SysFont("times new roman", 50)

        # Создаём текстовую поверхность, на которой будем отображать результат
        game_over_surface = my_font.render(
            "Вы набрали : " + str(score) + " очков", True, red
        )

        # Создаём четырёхугольник
        game_over_rect = game_over_surface.get_rect()

        # Указываем позицию текста
        game_over_rect.midtop = (window_x / 2, window_y / 4)

        # Это будет выводить текст на экран
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()

        # Устанавливаем задержку перед выходом
        time.sleep(2)

        # Выключаем Pygame
        pygame.quit()

        # Выход из программы
        quit()

    # Основная функция
    while True:

        # Опрос клавиатуры на нажатия
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = "UP"
                if event.key == pygame.K_DOWN:
                    change_to = "DOWN"
                if event.key == pygame.K_LEFT:
                    change_to = "LEFT"
                if event.key == pygame.K_RIGHT:
                    change_to = "RIGHT"

        # Реализация управления характерного для змейки
        if change_to == "UP" and direction != "DOWN":
            direction = "UP"
        if change_to == "DOWN" and direction != "UP":
            direction = "DOWN"
        if change_to == "LEFT" and direction != "RIGHT":
            direction = "LEFT"
        if change_to == "RIGHT" and direction != "LEFT":
            direction = "RIGHT"

        # Управление
        if direction == "UP":
            snake_position[1] -= 10
        if direction == "DOWN":
            snake_position[1] += 10
        if direction == "LEFT":
            snake_position[0] -= 10
        if direction == "RIGHT":
            snake_position[0] += 10

        # Механизм тела змеи
        # если змея съедает яблоко, то её тело увеличсивается, а счет увеличивается на 10
        snake_body.insert(0, list(snake_position))
        if (
            snake_position[0] == fruit_position[0]
            and snake_position[1] == fruit_position[1]
        ):
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [
                random.randrange(1, (window_x // 10)) * 10,
                random.randrange(1, (window_y // 10)) * 10,
            ]

        fruit_spawn = True
        game_window.fill(black)

        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(
            game_window,
            white,
            pygame.Rect(fruit_position[0], fruit_position[1], 10, 10),
        )

        # Условия конца игры
        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over()

        # Касание тела
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        # Непрерывно показываем счёт
        show_score(1, white, "times new roman", 20)

        # Обновление экрана
        pygame.display.update()

        # скорость обновления
        fps.tick(snake_speed)
