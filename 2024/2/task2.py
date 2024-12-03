
def are_differences_within_limit(lst):
    return all(1 <= abs(lst[i] - lst[i + 1]) <= 3 for i in range(len(lst) - 1))

def is_safe_raport(r):
    if r == sorted(r) or r == sorted(r, reverse=True):
        if are_differences_within_limit(r):
            return True

with open('input.txt', 'r') as file:

    safe_raport = 0

    for line in file:
        raport = list(map(int, line.strip().split()))
        if is_safe_raport(raport):
            safe_raport += 1
        else:
            for i in range(len(raport)):
                temp_raport = raport.copy()
                del temp_raport[i]
                if is_safe_raport(temp_raport):
                    safe_raport += 1
                    break


print("Answer 1:" , safe_raport)