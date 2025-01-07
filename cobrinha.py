import pygame
import random
import json

# Inicializando o Pygame
pygame.init()

# Definindo algumas cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Tamanho da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Configurando a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo da Cobrinha")

# Função para salvar o placar
def salvar_placar(score):
    try:
        with open("placar.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    data["highest_score"] = max(score, data.get("highest_score", 0))

    with open("placar.json", "w") as file:
        json.dump(data, file)

# Função para carregar o placar
def carregar_placar():
    try:
        with open("placar.json", "r") as file:
            data = json.load(file)
            return data.get("highest_score", 0)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0

# Classe base para o jogo
class GameObject:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x * GRID_SIZE, self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Classe para a cobrinha
class Snake(GameObject):
    def __init__(self, x, y):
        super().__init__(GREEN, x, y)
        self.body = [(x, y)]
        self.direction = (0, 1)

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body = [new_head] + self.body

    def set_direction(self, direction):
        if direction == "UP" and self.direction != (0, 1):
            self.direction = (0, -1)
        elif direction == "DOWN" and self.direction != (0, -1):
            self.direction = (0, 1)
        elif direction == "LEFT" and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif direction == "RIGHT" and self.direction != (-1, 0):
            self.direction = (1, 0)

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, self.color, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Classe para a comida
class Food(GameObject):
    def __init__(self):
        super().__init__(RED, 0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.x = random.randint(0, GRID_WIDTH - 1)
        self.y = random.randint(0, GRID_HEIGHT - 1)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x * GRID_SIZE, self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Função principal do jogo
def main():
    clock = pygame.time.Clock()
    snake = Snake(GRID_WIDTH // 2, GRID_HEIGHT // 2)
    food = Food()
    score = 0
    highest_score = carregar_placar()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.set_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.set_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    snake.set_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.set_direction("RIGHT")

        snake.move()

        # Verificando se a cobrinha colidiu com a comida
        if snake.body[0] == (food.x, food.y):
            food.randomize_position()
            snake.grow()
            score += 10

        # Verificando colisão com as paredes ou com o próprio corpo
        if not (0 <= snake.body[0][0] < GRID_WIDTH and 0 <= snake.body[0][1] < GRID_HEIGHT) or snake.body[0] in snake.body[1:]:
            running = False

        # Desenhando tudo
        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)

        # Exibindo o placar
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score} | High Score: {highest_score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(10)

    salvar_placar(score)
    pygame.quit()

if __name__ == "__main__":
    main()
