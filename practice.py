import random

numbers = [i for i in range(1, 46)]


lotto = [random.choice(numbers) for _ in range(6)]

print(sorted(lotto))
