# connect4.py

import pygame
import sys
from config import *
from game_logic import Connect4Game
from players import HumanPlayer, AIPlayer

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect4 Game")

font = pygame.font.SysFont("monospace", 50)

def draw_board(board):
    for c in range(COL):
        for r in range(ROW):
            pygame.draw.rect(screen, BLUE, (c*SQUARE, (r+1)*SQUARE, SQUARE, SQUARE))
            pygame.draw.circle(screen, BLACK, (c*SQUARE + SQUARE//2, (r+1)*SQUARE + SQUARE//2), RADIUS)

    for c in range(COL):
        for r in range(ROW):
            piece = board[r][c]
            if piece == 1:
                pygame.draw.circle(screen, RED,
                                   (c*SQUARE + SQUARE//2,
                                    HEIGHT - (r+1)*SQUARE + SQUARE//2),
                                   RADIUS)
            elif piece == 2:
                pygame.draw.circle(screen, YELLOW,
                                   (c*SQUARE + SQUARE//2,
                                    HEIGHT - (r+1)*SQUARE + SQUARE//2),
                                   RADIUS)

    pygame.display.update()


def main(mode="human-vs-ai"):
    game = Connect4Game()

    if mode == "human-vs-human":
        player1 = HumanPlayer(1)
        player2 = HumanPlayer(2)
    else:
        player1 = HumanPlayer(1)
        player2 = AIPlayer(2)

    turn = 0
    draw_board(game.board)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN \
               and isinstance([player1, player2][turn], HumanPlayer):

                x = event.pos[0]
                col = x // SQUARE

                if game.is_valid(col):
                    row = game.get_next_row(col)
                    game.drop_piece(row, col, turn+1)

                    if game.check_win(turn+1):
                        label = font.render(f"Player {turn+1} wins!",
                                            1,
                                            RED if turn == 0 else YELLOW)
                        screen.blit(label, (40, 10))
                        pygame.display.update()
                        pygame.time.wait(3000)
                        main(mode)
                        return

                    turn = 1 - turn
                    draw_board(game.board)

        # AI move
        if isinstance([player1, player2][turn], AIPlayer):
            pygame.time.wait(500)

            col = player2.get_move(game.board)
            if game.is_valid(col):
                row = game.get_next_row(col)
                game.drop_piece(row, col, 2)

                if game.check_win(2):
                    label = font.render("AI Wins!", 1, YELLOW)
                    screen.blit(label, (40, 10))
                    pygame.display.update()
                    pygame.time.wait(3000)
                    main(mode)
                    return

                turn = 0
                draw_board(game.board)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main("human-vs-ai")
