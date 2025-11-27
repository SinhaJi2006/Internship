import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("XO Game")

WHITE = (255, 255, 255)
BLACK = (0,0,0)
size = 200

board = [["","",""],
         ["","",""],
         ["","",""]]

player = "x"
font = pygame.font.Font(None,100)
run = True
game_over = False
winner = None


# ---------------------------
# FUNCTION TO CHECK WINNER
# ---------------------------
def check_winner(b):
    # Check rows
    for r in range(3):
        if b[r][0] == b[r][1] == b[r][2] != "":
            return b[r][0]

    # Check columns
    for c in range(3):
        if b[0][c] == b[1][c] == b[2][c] != "":
            return b[0][c]

    # Check diagonals
    if b[0][0] == b[1][1] == b[2][2] != "":
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != "":
        return b[0][2]

    return None


while run:
    screen.fill(WHITE)

    # Draw grid lines
    pygame.draw.line(screen,BLACK,(200,0),(200,600),5)
    pygame.draw.line(screen,BLACK,(400,0),(400,600),5)
    pygame.draw.line(screen,BLACK,(0,200),(600,200),5)
    pygame.draw.line(screen,BLACK,(0,400),(600,400),5)

    # Draw X/O on board
    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                text = font.render(board[row][col], True, BLACK)
                screen.blit(text, (col*size + 70, row*size + 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // 200
            col = mouse_x // 200

            if board[row][col] == "":
                board[row][col] = player

                # Check winner after move
                winner = check_winner(board)
                if winner:
                    game_over = True

                # Switch player
                player = "o" if player == "x" else "x"

    # Show winner message
    if game_over:
        win_font = pygame.font.Font(None, 80)
        text = win_font.render(f"{winner.upper()} wins!", True, (255, 0, 0))
        screen.blit(text, (180, 260))

    pygame.display.update()

pygame.quit()