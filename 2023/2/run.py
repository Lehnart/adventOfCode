class GameSet:

    def __init__(self, r: int, g: int, b: int):
        self.b = b
        self.r = r
        self.g = g


class Game:

    def __init__(self):
        self.sets = []
        self.min_r = 0
        self.min_g = 0
        self.min_b = 0

    def add(self, game_set: GameSet):
        if game_set.r > self.min_r:
            self.min_r = game_set.r
        if game_set.g > self.min_g:
            self.min_g = game_set.g
        if game_set.b > self.min_b:
            self.min_b = game_set.b

    def __repr__(self):
        return str((self.min_r, self.min_g, self.min_b))

games = []
with open("input.txt") as file:
    for line in file:
        raw_game = line.strip().split(":")[1].split(";")
        game = Game()
        for raw_set in raw_game:
            r, g, b = 0, 0, 0,
            for raw_color in raw_set.strip().split(","):
                raw_color = raw_color.strip().split(" ")
                if raw_color[1] == "green":
                    g = int(raw_color[0])
                elif raw_color[1] == "red":
                    r = int(raw_color[0])
                elif raw_color[1] == "blue":
                    b = int(raw_color[0])
                else:
                    raise Exception()
            game_set = GameSet(r, g, b)
            game.add(game_set)
        games.append(game)
ids = 0
powers = 0
for i, game in enumerate(games):
    powers += game.min_r*game.min_g*game.min_b
    if game.min_r <= 12 and game.min_g <= 13 and game.min_b <= 14 :
       ids += 1 + i
print(ids)
print(powers)