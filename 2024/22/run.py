secrets = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        secrets.append(int(line))

secret_diff_set = set()

def compute_next_secret(secret):
    next_secret = secret 
    next_secret *= 64 
    next_secret = next_secret ^ secret 
    next_secret = next_secret % 16777216

    temp = next_secret
    next_secret //= 32
    next_secret = next_secret ^ temp 
    next_secret = next_secret % 16777216
 
    temp = next_secret
    next_secret *= 2048
    next_secret = next_secret ^ temp 
    next_secret = next_secret % 16777216

    return next_secret

count = 0 
for secret in secrets:
    sequence = []
    next_secret = secret
    for _ in range(2000):
        new_secret = compute_next_secret(next_secret)
        if len(sequence) < 4:
            sequence.append(new_secret - next_secret)
        else : 
            sequence.pop(0)
            sequence.append(new_secret-next_secret)
            secret_diff_set.add(tuple(sequence))
        next_secret = new_secret

    print(next_secret)
    count += next_secret
print(count)
print(len(secret_diff_set))