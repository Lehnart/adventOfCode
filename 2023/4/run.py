score = 0
card_scores = []
card_winning_numbers_counts = []
with open("input.txt") as file:
    for line in file:
        card_score = 0
        card_winning_number_count = 0
        card = line.strip().split(":")[1]
        winning_numbers_raw, numbers_raw = card.split("|")
        winning_numbers = [int(wn) for wn in winning_numbers_raw.strip().replace("  ", " ").split(" ")]
        numbers = [int(n) for n in numbers_raw.strip().replace("  ", " ").split(" ")]
        for winning_number in winning_numbers:
            if winning_number in numbers:
                card_winning_number_count += 1
                if card_score == 0:
                    card_score = 1
                else:
                    card_score *= 2
        card_scores.append(card_score)
        card_winning_numbers_counts.append(card_winning_number_count)
        score += card_score

card_counts = [1 for _ in range(len(card_scores))]
print(card_winning_numbers_counts)
for i,card_winning_number_count in enumerate(card_winning_numbers_counts):
    for j in range(card_winning_number_count):
        card_counts[i+j+1] += card_counts[i]

print (score)
print(sum(card_counts))