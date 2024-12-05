
def get_page_ordering():
    with open("page_ordering.txt", 'r') as file:
        lines = file.readlines()
        return [tuple(map(int, line.strip().split('|'))) for line in lines]


def get_updates():
    with open("updates.txt", 'r') as file:
        return [list(map(int, line.strip().split(','))) for line in file]


def find_page_index(update, number):
    try:
        return update.index(number)
    except ValueError:
        return -1


def check_page_ordering(update, rule):
    first_index = find_page_index(update, rule[0])
    second_index = find_page_index(update, rule[1])
    if first_index >=0  and second_index >= 0:
        if first_index < second_index:
            return True
        else:
            return False
    else:
        return True

def check_update(update, rules):
    check_sum = len(rules)
    correctness_page = 0
    for rule in rules:
        if check_page_ordering(update, rule):
            correctness_page += 1
    if check_sum == correctness_page:
        return True
    else:
        return False

def swap_if_incorrect(update, rule):
    first_index = find_page_index(update, rule[0])
    second_index = find_page_index(update, rule[1])
    if first_index >=0  and second_index >= 0:
        if first_index > second_index:
            update[first_index], update[second_index] = update[second_index], update[first_index]

def fix_ordering(update, rules):
    flag = True
    for rule in rules:
        if not check_page_ordering(update, rule):
            swap_if_incorrect(update, rule)
            flag = False

    if not flag:
        fix_ordering(update, rules)

def get_middle_value(update):
    middle_index = len(update) // 2
    return update[middle_index]


page_ordering = get_page_ordering()
updates = get_updates()
summary = 0
invalid_updates = []

for update  in updates:
    if not check_update(update, page_ordering):
        invalid_updates.append(update)

for invalid_update in invalid_updates:
    fix_ordering(invalid_update, page_ordering)

for update in invalid_updates:
    summary += get_middle_value(update)


print("Answer: ", summary)
