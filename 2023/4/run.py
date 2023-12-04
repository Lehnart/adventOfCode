score = 0
with open("input.txt") as file:
    for line in file:
        card_score = 0
        card = line.strip().split(":")[1]
        winning_numbers_raw, numbers_raw = card.split("|")
        winning_numbers = [int(wn) for wn in winning_numbers_raw.strip().replace("  ", " ").split(" ")]
        numbers = [int(n) for n in numbers_raw.strip().replace("  ", " ").split(" ")]
        for winning_number in winning_numbers:
            if winning_number in numbers:
                if card_score == 0:
                    card_score = 1
                else:
                    card_score *= 2
        score += card_score
print (score)