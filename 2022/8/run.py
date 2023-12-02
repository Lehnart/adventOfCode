class Tree:

    def __init__(self, height: int):
        self.is_visible = False
        self.height = height
        self.score = 0

    def __repr__(self):
        return str(self.height)


trees = []
with open("input.txt") as file:
    for line in file.readlines():
        line = line.strip()
        trees.append([])
        for c in line:
            trees[-1].append(Tree(int(c)))

for row in trees:
    current_height = row[0].height
    row[0].is_visible = True
    for tree in row[1:]:
        if current_height < tree.height:
            current_height = tree.height
            tree.is_visible = True

for row in trees:
    row = row[::-1]
    current_height = row[0].height
    row[0].is_visible = True
    for tree in row[1:]:
        if current_height < tree.height:
            current_height = tree.height
            tree.is_visible = True

cols = [[row[i] for row in trees] for i in range(len(trees[0]))]
for col in cols:
    current_height = col[0].height
    col[0].is_visible = True
    for tree in col[1:]:
        if current_height < tree.height:
            current_height = tree.height
            tree.is_visible = True

for col in cols:
    col = col[::-1]
    current_height = col[0].height
    col[0].is_visible = True
    for tree in col[1:]:
        if current_height < tree.height:
            current_height = tree.height
            tree.is_visible = True

n = 0
for row in trees:
    for tree in row:
        if tree.is_visible:
            n += 1
print(n)


def get_top_view(i0, j0, trees):
    view = []
    for j in range(len(trees)):
        if j < j0:
            view.append(trees[j][i0])
    return view[::-1]


def get_down_view(i0, j0, trees):
    view = []
    for j in range(len(trees)):
        if j > j0:
            view.append(trees[j][i0])
    return view


def get_left_view(i0, j0, trees):
    view = []
    for i in range(len(trees[0])):
        if i < i0:
            view.append(trees[j0][i])
    return view[::-1]


def get_right_view(i0, j0, trees):
    view = []
    for i in range(len(trees[0])):
        if i > i0:
            view.append(trees[j0][i])
    return view


def get_view_range(view, height):
    view_range = 0
    for h in view:
        view_range += 1
        if h.height >= height:
            return view_range
    return view_range


max = 0
for j in range(len(trees)):
    for i in range(len(trees[j])):
        current_height = trees[j][i].height
        dv = get_view_range(get_down_view(i, j, trees), current_height)
        tv = get_view_range(get_top_view(i, j, trees), current_height)
        lv = get_view_range(get_left_view(i, j, trees), current_height)
        rv = get_view_range(get_right_view(i, j, trees), current_height)
        trees[j][i].score = dv * tv * lv * rv
        if trees[j][i].score > max:
            max = trees[j][i].score
print(max)
