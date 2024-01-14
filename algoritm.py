from constantes import Score

def alphabeta(t, fgenerator, fplay, feval, is_game_finished, alpha, beta, height):
    def alpha_beta_rec(t, a, b, h):
        is_computer = h%2 == 0
        is_finished = is_game_finished(t, moves)
        moves = fgenerator(t)
        if is_finished == 1:
            if is_computer:
                return (-Score.inifinity.value + h, [])
            else:
                return (Score.inifinity.value - 1 - h, [])
        else:
            if is_finished == 0: return (0, [])
            else:
                if is_computer:
                    if h == height: return (feval(t), [])
                    else:              

    eval, moves = alpha_beta_rec(t, alpha, beta, 0)
    if moves: return moves.pop(0)
    else: return None