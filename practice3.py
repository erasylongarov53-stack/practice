import math
import random


def hill_climbing(values, start):
    current = start
    while True:
        neighbors = []
        if current > 0:
            neighbors.append(current - 1)
        if current < len(values) - 1:
            neighbors.append(current + 1)

        best_neighbor = max(neighbors, key=lambda idx: values[idx])

        if values[best_neighbor] > values[current]:
            current = best_neighbor
        else:
            break

    return current, values[current]


def random_restart(values, attempts=5):
    best_idx, best_val = None, float("-inf")
    for _ in range(attempts):
        random_start = random.randint(0, len(values) - 1)
        idx, val = hill_climbing(values, start=random_start)
        if val > best_val:
            best_idx, best_val = idx, val
    return best_idx, best_val


def random_neighbor(current, length):
    neighbors = []
    if current > 0:
        neighbors.append(current - 1)
    if current < length - 1:
        neighbors.append(current + 1)
    return random.choice(neighbors)


def anneal(values, start=0, temp=10.0, cooling_rate=0.95, min_temp=0.01):
    current = start
    current_temp = temp

    while current_temp > min_temp:
        nxt = random_neighbor(current, len(values))
        delta = values[nxt] - values[current]

        if delta > 0 or random.random() < math.exp(delta / current_temp):
            current = nxt

        current_temp *= cooling_rate

    return current, values[current]


values1 = [1, 3, 5, 8, 6, 4, 2]
print("2-ТАПСЫРМА:")
for s in [0, 2, 4, 6]:
    idx, val = hill_climbing(values1, start=s)
    print(f"Start = {s} -> Index: {idx}, Value: {val}")

values2 = [1, 4, 7, 5, 3, 6, 9, 8]
print("\n3-ТАПСЫРМА:")
for s in [0, 4]:
    idx, val = hill_climbing(values2, start=s)
    print(f"Start = {s} -> Index: {idx}, Value: {val}")

print("\n4-ТАПСЫРМА:")
for exp in range(1, 4):
    random.seed(exp)
    b_idx, b_val = random_restart(values2, attempts=5)
    print(f"Exp {exp} -> Best Index: {b_idx}, Best Value: {b_val}")

print("\n5-ТАПСЫРМА:")
for run in range(1, 6):
    final_idx, final_val = anneal(values2, start=0)
    print(f"Run {run} -> Final Index: {final_idx}, Final Value: {final_val}")
