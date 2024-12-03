from collections import Counter

with open('input.txt', 'r') as file:
    left_list = []
    right_list = []

    for line in file:
        numbers = line.strip().split()
        if len(numbers) == 2:
            left_list.append(int(numbers[0]))
            right_list.append(int(numbers[1]))

left_list.sort()
right_list.sort()

summary = 0

for i in range(len(left_list)):
    a = left_list[i]
    b = right_list[i]
    difference = abs(a - b)
    summary += difference

summary2 = 0
right_count = Counter(right_list)

for number in left_list:
    occurrences = right_count.get(number, 0)
    summary2 += number * occurrences

print("Answer 1:", summary)
print("Answer 2:", summary2)