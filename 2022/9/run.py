class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def pos(self):
        return (self.x, self.y)

    def __hash__(self):
        return hash(self.pos())


moves = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}
TAIL_LENGTH = 9
H = Position(0, 0)
TS = [Position(0, 0) for _ in range(TAIL_LENGTH)]
positions = set()
with open("input.txt") as file:
    for line in file:
        direction, count = line.strip().split()
        count = int(count)
        move = moves[direction]
        for _ in range(count):
            H.x += move[0]
            H.y += move[1]
            for i in range(TAIL_LENGTH):
                T = TS[i]
                next_knot = H if i == 0 else TS[i - 1]
                dx = next_knot.x - T.x
                dy = next_knot.y - T.y
                if abs(dx) >= 2 or abs(dy) >= 2:
                    mx, my = dx, dy
                    if mx == 2:
                        mx = 1
                    if mx == -2:
                        mx = -1
                    if my == 2:
                        my = 1
                    if my == -2:
                        my = -1
                    T.x += mx
                    T.y += my
                if i == TAIL_LENGTH - 1:
                    positions.add(T.pos())
print(len(positions))
position_list = list(positions)
position_list = [(p[0] + 195, p[1] + 232) for p in position_list]
