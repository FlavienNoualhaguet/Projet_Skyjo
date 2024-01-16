from constantes import Score

def alphabeta(t, fgenerator, fplay, feval, is_game_finished, alpha, beta, height):
    # AlphaBeta Rec
    def alpha_beta_rec(t, a, b, h):
        is_computer = h%2 == 0
        moves = fgenerator(t)
        is_finished = is_game_finished(t, moves)
        if is_finished == 1:
            if is_computer:
                return (-Score.infinity.value + h, [])
            else:
                return (Score.infinity.value - 1 - h, [])
        else:
            if is_finished == 0: return (0, [])
            else:
                if is_computer:
                    if h == height: return (feval(t), [])
                    else:
                        s, acc = a, []
                        for move in moves:
                            new_state         = fplay(move, t)
                            new_eval, new_acc = alpha_beta_rec(new_state, s, b, h+1)
                            if s < new_eval:
                                if b <= new_eval:
                                    new_acc.insert(0, move) 
                                    return (new_eval, new_acc)
                                else:
                                    s = new_eval
                                    new_acc.insert(0, move)
                                    acc = new_acc
                            else:
                                continue
                        return s, acc
                else:
                    if h == height: return (feval(t), [])
                    else:
                        s, acc = b, []
                        for move in moves:
                            new_state         = fplay(move, t)
                            new_eval, new_acc = alpha_beta_rec(new_state, a, s, h+1)
                            if new_eval < s:
                                if new_eval <= a:
                                    new_acc.insert(0, move) 
                                    return (new_eval, new_acc)
                                else:
                                    s = new_eval
                                    new_acc.insert(0, move)
                                    acc = new_acc
                            else:
                                continue
                        return s, acc
    # Fin AlphaBeta Rec
                    
    eval, moves = alpha_beta_rec(t, alpha, beta, 0)
    if moves: return moves.pop(0)
    else: return None