def minimax(self, player, depth = 0) :
    if player == "o":
        best = -10
    else:
        best = 10
    if self.complete():
        if self.getWinner() == "x": # 'X' is the computer
            return -10 + depth, None
        elif self.getWinner() == "tie":
            return 0, None
        elif self.getWinner() == "o" : # 'O' is the human
            return 10 - depth, None
    for move in self.getAvailableMoves() :
        self.makeMove(move, player)
        val, _ = self.minimax(self.getEnemyPlayer(player), depth+1)
        print(val)

        self.makeMove(move, ".")

        if player == "o" :
            if val > best :
                best, bestMove = val, move
        else :
            if val < best :
                best, bestMove = val, move

    return best, bestMove
