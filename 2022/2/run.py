class RockPaperScissorGame:

    def __init__(self):
        self.score = 0
        self.score2 = 0
    def play(self, opponent_move:str, move:str):
        moves = opponent_move + move
        if moves == "AX":
            self.score += 4
        if moves == "AY":
            self.score += 8
        if moves == "AZ":
            self.score += 3
        if moves == "BX":
            self.score += 1
        if moves == "BY":
            self.score += 5
        if moves == "BZ":
            self.score += 9
        if moves == "CX":
            self.score += 7
        if moves == "CY":
            self.score += 2
        if moves == "CZ":
            self.score += 6

    def play2(self, opponent_move:str, result:str):
        moves = opponent_move + result
        if moves == "AX":
            self.score2 += 3
        if moves == "AY":
            self.score2 += 4
        if moves == "AZ":
            self.score2 += 8
        if moves == "BX":
            self.score2 += 1
        if moves == "BY":
            self.score2 += 5
        if moves == "BZ":
            self.score2 += 9
        if moves == "CX":
            self.score2 += 2
        if moves == "CY":
            self.score2 += 6
        if moves == "CZ":
            self.score2 += 7

rps_game = RockPaperScissorGame()
with open("input.txt") as input_file:
    for line in input_file:
        opp_move, move = line.strip().split(" ")
        rps_game.play(opp_move, move)
        rps_game.play2(opp_move, move)
print(rps_game.score)
print(rps_game.score2)