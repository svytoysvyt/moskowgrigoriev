import os
import sys
import random
import pygame


pygame.init()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
pigs = pygame.sprite.Group()
foods = pygame.sprite.Group()
WIDTH = 1800
HEIGHT = 1000
FPS = 60
RADB = 0
RADL = 1000
DEAD = 0
FOOD = 0
IT = 1
CLIVES = 0
LIVE = 0
LIVES = 50
CDEAD = 0
CLIVE = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
IMAGE = 'data/back.png'
example = open(f'example.txt', 'w')
work = open('work.txt', 'w')


def load_image(name):
    """
    функция загрузка изображения

    """
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Board:
    """

    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size, color1, color2):

        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.color = [color1, color2]

    def render(self, surface: pygame.Surface):

        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if (row + column) % 2 == 0:
                    pygame.draw.rect(surface=surface, color=self.color[0], rect=(
                        self.left + self.cell_size * column,
                        self.top + self.cell_size * row,
                        self.cell_size,
                        self.cell_size
                    ))
                else:
                    pygame.draw.rect(surface=surface, color=self.color[1], rect=(
                        self.left + self.cell_size * column,
                        self.top + self.cell_size * row,
                        self.cell_size,
                        self.cell_size
                    ))


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__()
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class Food(pygame.sprite.Sprite):
    """
gyhglk
    """
    IMAGE = load_image("food.png")

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Food.IMAGE, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(165, 1635)
        self.rect.y = random.randint(65, 935)



class Pig(pygame.sprite.Sprite):
    """
pperpoe
    """
    IMAGE = load_image("white.png")

    def __init__(self, types, *args):
        global RADL
        global RADB
        pygame.sprite.Sprite.__init__(self)
        self.radius = 1

        if types == 0:
            self.radius = random.randint(12, 20)
        else:
            self.radius = args[0]
        if self.radius < RADL:
            RADL = self.radius
        if self.radius > RADB:
            RADB = self.radius
        self.image = pygame.transform.scale(Pig.IMAGE, (self.radius * 2, self.radius * 2))
        self.fast = 110 // self.radius
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(200, 1600)
        self.rect.y = random.randint(100, 900)
        self.eat = 0
        self.vx = random.randint(-self.fast, self.fast)
        self.vy = int((self.fast ** 2 - self.vx ** 2) ** 0.5 // random.choice([-1, 1]))

    def update(self, types, *args):
        global DEAD
        global LIVE
        global CDEAD
        global LIVES
        global CLIVE
        global CLIVES
        if types == 0:
            self.rect = self.rect.move(self.vx, self.vy)
            if pygame.sprite.spritecollideany(self, horizontal_borders):
                self.vy *= -1
            if pygame.sprite.spritecollideany(self, vertical_borders):
                self.vx *= -1
            self.eat += len(pygame.sprite.spritecollide(self, foods, True))
            for er in pygame.sprite.spritecollide(self, pigs, False):
                if 1.5 * er.rect.width <= self.rect.width <= 2.5 * er.rect.width:
                    self.eat += er.rect.width // 4
                    example.write(f'Бактерия с координатами:[{self.rect[0] + self.radius - 150}, {self.rect[1] + self.radius - 50}]\n'
                                  f'с радиусом {self.radius}, со скоростью {200 // self.rect[2]} и с едой {self.eat}\n'
                                  f'уничтожила бактерию с радиусом {er.rect[2] // 2}, со скоростью {200 // er.rect[2]}\n'
                                  f'в время {pygame.time.get_ticks()} миллисекунд\n \n')
                    work.write(f'1, {self.rect[0] + self.radius - 150}, {self.rect[1] + self.radius - 50},'
                               f' {self.radius}, {200 // self.rect[2]}, {er.rect[2] // 2}, {self.eat},'
                               f' {pygame.time.get_ticks()}, \n')
                    DEAD += 1
                    LIVES -= 1
                    CDEAD += er.rect[2] // 2
                    er.kill()
        elif types == 1:
            if self.eat < self.radius // 2:
                example.write(
                    f'Бактерия с координатами:[{self.rect[0] + self.radius - 150}, {self.rect[1] + self.radius - 50}]\n'
                    f'с радиусом {self.radius}, со скоростью {self.rect[2] // 4} и с едой {self.eat}\n'
                    f'умерла от голода во время {pygame.time.get_ticks()} миллисекунд\n \n')
                work.write(
                    f'2,  {self.rect[0] + self.radius - 150}, {self.rect[1] + self.radius - 50}, '
                    f'{self.radius}, {self.eat}, {pygame.time.get_ticks()}, \n')
                DEAD += 1
                LIVES -= 1
                CDEAD += self.rect[2] // 2
                self.kill()
            else:
                LIVE += 1
                CLIVE += self.rect[2] // 2
                if 1 + random.random() <= self.eat / (self.radius // 2):
                    a = 0
                    if random.randint(1, 3) == 1:
                        a = random.randint(self.rect[2] // -6, self.rect[2] // 6)

                        for j in range(random.randint(1, self.eat / (self.radius // 2) // 1)):
                            if self.rect[2] // 2 + a > 4:
                                d = self.rect[2] // 2 + a
                                pigs.add(Pig(1, d))
                                work.write(f'4, {self.rect.x}, {self.rect.y}, {self.rect.width // 2},'
                                           f' {d - self.rect.width // 2}, {d}, \n')
                                example.write(f'бактерия с радиусом {self.rect.width // 2} создала бактерию с радиусом {d}'
                                              f' при мутации {d - self.rect.width // 2} \n\n')
                                LIVES += 1
                                CLIVES += self.rect[2] // 2 + a
                            a = 0
                            if random.randint(1, 3) == 1:
                                a = random.randint(self.rect[2] // -6, self.rect[2] // 6)
            self.eat = 0


if __name__ == '__main__':
    u = 0
    pygame.display.set_caption('симулятор мутации')
    Border(150, 53, WIDTH - 150, 53)
    Border(150, HEIGHT - 53, WIDTH - 150, HEIGHT - 53)
    Border(153, 50, 153, HEIGHT - 50)
    Border(WIDTH - 153, 50, WIDTH - 153, HEIGHT - 50)
    Border(150, 50, WIDTH - 150, 50)
    Border(150, HEIGHT - 50, WIDTH - 150, HEIGHT - 50)
    Border(150, 50, 150, HEIGHT - 50)
    Border(WIDTH - 150, 50, WIDTH - 150, HEIGHT - 50)
    Border(150, 47, WIDTH - 150, 47)
    Border(150, HEIGHT - 47, WIDTH - 150, HEIGHT - 47)
    Border(147, 50, 147, HEIGHT - 50)
    Border(WIDTH - 147, 50, WIDTH - 147, HEIGHT - 50)
    for i in range(50):
        pigs.add(Pig(0))
    FOOD = random.randint(250, 500)
    for i in range(FOOD):
        foods.add(Food())
    back = pygame.image.load(IMAGE)
    back_rect = back.get_rect()
    board = Board(300, 180)
    clock = pygame.time.Clock()
    board.set_view(150, 50, 5, 'white', 'pink')
    running = True
    f2 = pygame.font.SysFont('serif', 48)
    f1 = pygame.font.SysFont('serif', 80)
    text2 = f2.render(f'ЦИКЛ № {IT} (ИЗ 1080)', True, (153, 102, 204))
    text1 = f2.render(f'ЖИВО: {LIVES}', True, (206, 210, 58))
    text3 = f1.render(f'{(20000 - (pygame.time.get_ticks()) % 20000) // 1000 + 1}', True, (0, 125, 255))
    screen.blit(back, back_rect)
    board.render(screen)
    o = pygame.time.get_ticks()
    pygame.time.set_timer(pygame.USEREVENT, 20000, 1080)
    pygame.time.set_timer(pygame.QUIT, 21601000, 1)
    while running:
        screen.blit(back, back_rect)
        screen.blit(text2, (150, 5))
        screen.blit(text1, (600, 5))
        screen.blit(text3, (20, 5))
        board.render(screen)
        foods.draw(screen)
        pigs.draw(screen)
        pigs.update(0)
        text3 = f1.render(f'{(20000 - (pygame.time.get_ticks() - o) % 20000) // 1000 + 1}', True, (0, 125, 255))
        text1 = f2.render(f'ЖИВО: {LIVES}', True, (206, 210, 58))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                pigs.update(1)
                print(DEAD, CDEAD, LIVE, CLIVE)
                if DEAD == 0:
                    DEADU = 0
                else:
                    DEADU = CDEAD / DEAD
                if LIVE == 0:
                    LIVEU = 0
                else:
                    LIVEU = CLIVE / LIVE
                if LIVES == LIVE:
                    LIVESU = 0
                else:
                    LIVESU = CLIVES / (LIVES - LIVE)
                work.write(f'3, {IT}, {DEAD}, {DEADU}, {LIVE}, {LIVEU},'
                           f' {LIVES  - LIVE}, {DEAD + LIVE}, {(CDEAD + CLIVE) / (DEAD + LIVE)}, {LIVES},'
                           f' {LIVESU}, {FOOD}, \n')
                example.write(f'погибло {DEAD},средний размер погибшего {DEADU},'
                              f'выжило {LIVE},средний размер выжившего {LIVEU}\n'
                              f' количество новых {LIVES  - LIVE} , их размер {LIVESU} '
                              f'и начальном размере {(CDEAD + CLIVE)/ (DEAD + LIVE)} '
                              f'с количеством добавленной пищи {FOOD}\nЗАКОНЧЕН ЦИКЛ № {IT}\n\n\n')

#                FOOD = random.randint(250 * 0.35 // 1 + DEAD // 2, 500 * 0.7 // 1 + DEAD)):
                FOOD = random.randint(200, 400)
                for i in range(FOOD):
                    foods.add(Food())
                DEAD = 0
                CDEAD = 0
                LIVE = 0
                CLIVE = 0
                CLIVES = 0
                IT += 1
                text2 = f2.render(f'ЦИКЛ № {IT}(ИЗ 1080)', True, (153, 102, 204))
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    example.write(f'минимальный радиус: {RADL}\nмаксимальный радиус:{RADB}')
    work.write(f'5, {RADL}, {RADB}')
    example.close()
    work.close()
