import random

rolls = 20
count_6 = 0
count_1 = 0
two_sixes_row = 0

previous_roll = 0

for i in range(rolls):
    current_roll = random.randint(1, 6)
    print("Roll", i + 1, ":", current_roll)

    if current_roll == 6:
        count_6 += 1

    if current_roll == 1:
        count_1 += 1

    if previous_roll == 6 and current_roll == 6:
        two_sixes_row += 1

    previous_roll = current_roll

print("\nStatistics:")
print("Number of times 6 was rolled:", count_6)
print("Number of times 1 was rolled:", count_1)
print("Number of times two 6s occurred in a row:", two_sixes_row)
