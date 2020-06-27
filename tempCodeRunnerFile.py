clock.tick(FPS)
game = Avalam_Game()
game.draw_board()
game.pawn_position()
for event in pygame.event.get():  
    if event.type == pygame.QUIT:  
        run = False  
    elif event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        column = pos[0] // (WIDTH + SPACE)
        row = pos[1] // (HEIGHT + SPACE)
        move[row,column].append(1)
        game.can_move((row,column))
    
pygame.display.flip()