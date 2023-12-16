import enum
from typing import Tuple

grid = []


class Direction(enum.Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Beam:

    def __init__(self, direction: Direction, pos: Tuple[int, int]):
        self.direction = direction
        self.pos = pos

    def copy(self):
        return Beam(self.direction, self.pos)

    def x(self):
        return self.pos[0]

    def y(self):
        return self.pos[1]

    def next_pos(self):
        if self.direction == Direction.UP:
            return self.x(), self.y() - 1
        if self.direction == Direction.RIGHT:
            return self.x() + 1, self.y()
        if self.direction == Direction.DOWN:
            return self.x(), self.y() + 1
        if self.direction == Direction.LEFT:
            return self.x() - 1, self.y()


with open("input.txt") as file:
    for line in file:
        grid.append([])
        for c in line.strip():
            grid[-1].append(c)

starting_beams = []
for y in range(len(grid)):
    starting_beams.append(Beam(Direction.RIGHT, (0, y)))
    starting_beams.append(Beam(Direction.LEFT, (len(grid[0]) - 1, y)))

for x in range(len(grid[0])):
    starting_beams.append(Beam(Direction.DOWN, (x, 0)))
    starting_beams.append(Beam(Direction.UP, (x, len(grid) - 1)))

max_count = 0
for starting_beam in starting_beams:
    cells = set()
    previous_cells = cells.copy()

    count = 0
    beams = [starting_beam]
    while beams:
        count += 1
        new_beams = []

        to_remove = []
        for i in range(len(beams)):
            beam = beams[i]
            if beam.x() < 0 or beam.x() > len(grid) - 1 or beam.y() < 0 or beam.y() > len(grid) - 1:
                to_remove.append(i)
            if (beam.x(), beam.y(), beam.direction) in cells:
                to_remove.append(i)

        for j in to_remove[::-1]:
            beams.pop(j)

        for beam in beams:
            cells.add((beam.x(), beam.y(), beam.direction))

        for beam in beams:
            c = grid[beam.y()][beam.x()]
            if c == ".":
                beam.pos = beam.next_pos()
            elif c == "\\":
                if beam.direction == Direction.RIGHT:
                    beam.direction = Direction.DOWN

                elif beam.direction == Direction.DOWN:
                    beam.direction = Direction.RIGHT

                elif beam.direction == Direction.LEFT:
                    beam.direction = Direction.UP

                elif beam.direction == Direction.UP:
                    beam.direction = Direction.LEFT

                else:
                    raise Exception
                beam.pos = beam.next_pos()

            elif c == "/":
                if beam.direction == Direction.RIGHT:
                    beam.direction = Direction.UP

                elif beam.direction == Direction.DOWN:
                    beam.direction = Direction.LEFT

                elif beam.direction == Direction.LEFT:
                    beam.direction = Direction.DOWN

                elif beam.direction == Direction.UP:
                    beam.direction = Direction.RIGHT

                else:
                    raise Exception
                beam.pos = beam.next_pos()

            elif c == "-":
                if beam.direction in [Direction.RIGHT, Direction.LEFT]:
                    beam.pos = beam.next_pos()

                elif beam.direction in [Direction.UP, Direction.DOWN]:
                    beam.direction = Direction.LEFT
                    new_beam = beam.copy()
                    new_beam.direction = Direction.RIGHT
                    new_beam.next_pos()
                    beam.pos = beam.next_pos()
                    new_beams.append(new_beam)
                else:
                    raise Exception

            elif c == "|":
                if beam.direction in [Direction.UP, Direction.DOWN]:
                    beam.pos = beam.next_pos()

                elif beam.direction in [Direction.LEFT, Direction.RIGHT]:
                    beam.direction = Direction.UP
                    new_beam = beam.copy()
                    new_beam.direction = Direction.DOWN
                    beam.pos = beam.next_pos()
                    new_beam.next_pos()
                    new_beams.append(new_beam)
                else:
                    raise Exception

        beams.extend(new_beams)
        new_beams.clear()

    reduced_cells = set()
    for cell in cells:
        reduced_cells.add((cell[0], cell[1]))
    if max_count < len(reduced_cells):
        max_count = len(reduced_cells)

print(max_count)
