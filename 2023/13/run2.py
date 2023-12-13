grids = [[]]
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        if line == "":
            grids.append([])
        else:
            grids[-1].append(line)

somme = 0
for grid in grids:
    similar_adjacent_row_indices = []
    similar_adjacent_col_indices = []

    for row_index in range(len(grid) - 1):
        if grid[row_index] == grid[row_index + 1]:
            similar_adjacent_row_indices.append((row_index, row_index + 1, False))
        else:
            diff = [1 if grid[row_index][i] != grid[row_index + 1][i] else 0 for i in range(len(grid[0]))]
            if sum(diff) == 1:
                similar_adjacent_row_indices.append((row_index, row_index + 1, True))

    for col_index in range(len(grid[0]) - 1):
        lcol = [r[col_index] for r in grid]
        rcol = [r[col_index + 1] for r in grid]
        if lcol == rcol:
            similar_adjacent_col_indices.append((col_index, col_index + 1, False))
        else:
            diff = [1 if lcol[i] != rcol[i] else 0 for i in range(len(grid))]
            if sum(diff) == 1:
                similar_adjacent_col_indices.append((col_index, col_index + 1, True))

    mirror_rows = []
    mirror_cols = []

    for lri, rri, smudge in similar_adjacent_row_indices:
        nlri = lri - 1
        nrri = rri + 1
        is_good = True
        is_smudge_found = smudge
        while not (nlri < 0 or nrri > len(grid) - 1):
            if grid[nlri] != grid[nrri]:
                if not is_smudge_found:
                    diff = [1 if grid[nlri][i] != grid[nrri][i] else 0 for i in range(len(grid[0]))]
                    if sum(diff) != 1:
                        is_good = False
                        break
                    else:
                        is_smudge_found = True
                else:
                    is_good = False
                    break
            nlri = nlri - 1
            nrri = nrri + 1
        if is_good and is_smudge_found:
            mirror_rows.append((lri, rri))

    for lci, rci, smudge in similar_adjacent_col_indices:
        nlci = lci - 1
        nrci = rci + 1
        is_good = True
        is_smudge_found = smudge
        while not (nlci < 0 or nrci > len(grid[0]) - 1):
            lcol = [r[nlci] for r in grid]
            rcol = [r[nrci] for r in grid]
            if lcol != rcol:
                if not is_smudge_found:
                    diff = [1 if lcol[i] != rcol[i] else 0 for i in range(len(grid))]
                    if sum(diff) != 1:
                        is_good = False
                        break
                    else:
                        is_smudge_found = True
                else:
                    is_good = False
                    break
            nlci = nlci - 1
            nrci = nrci + 1
        if is_good and is_smudge_found:
            mirror_cols.append((lci, rci))

    if len(mirror_rows) > 1 or len(mirror_cols) > 1 or (len(mirror_rows) == 1 and len(mirror_cols) == 1):
        raise Exception

    if mirror_rows:
        somme += 100 * (mirror_rows[0][0] + 1)
    elif mirror_cols:
        somme += (mirror_cols[0][0] + 1)
    else:
        raise Exception
    print(mirror_rows)
    print(mirror_cols)
    print()
    mirror_rows.clear()
    mirror_cols.clear()
    similar_adjacent_row_indices.clear()
    similar_adjacent_col_indices.clear()

print(somme)
