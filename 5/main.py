def read_input(filename):
    data = ""
    with open(filename, "r") as file:
        data = file.read()

    rows = data.strip().split("\n")
    rules = []
    updates = []
    for row in rows:
        if "|" in row:
            rule = tuple(row.split("|"))
            rules.append(rule)
        elif "," in row:
            updates.append(row.split(","))
    return rules, updates


def get_index(value, search_list):
    try:
        return search_list.index(value)
    except ValueError:
        return -1


def get_middle(updates):
    mid_idx = int((len(updates) - 1) / 2)
    return int(updates[mid_idx])


def check_valid_update(update, rules):
    for rule in rules:
        first_index = get_index(rule[0], update)
        second_index = get_index(rule[1], update)
        if first_index == -1 or second_index == -1:
            continue
        if second_index < first_index:
            return False
    return True


def find_broken_rules(update, rules):
    invalid_rules = []
    for rule in rules:
        first_index = get_index(rule[0], update)
        second_index = get_index(rule[1], update)
        if first_index == -1 or second_index == -1:
            continue
        if second_index < first_index:
            invalid_rules.append(rule)
    return invalid_rules


def find_valid_updates(updates, rules):
    total = 0
    invalid_updates = []
    for update in updates:
        print(update)
        if check_valid_update(update, rules):
            total += get_middle(update)
        else:
            invalid_updates.append(update)
    print(total)
    return invalid_updates


def fix_update(update, rules):
    fixed_rules = []
    for rule in rules:
        first_not_in = rule[0] not in fixed_rules
        second_not_in = rule[1] not in fixed_rules
        neither_in = first_not_in and second_not_in
        if neither_in:
            fixed_rules.append(rule[0])
            fixed_rules.append(rule[1])
        else:
            if first_not_in:
                fixed_rules.insert(0, rule[0])
            if second_not_in:
                fixed_rules.append(rule[1])

            # else:
            #     first_idx = get_index(rule[0], fixed)
            #     second_idx = get_index(rule[1], fixed)

    print(rules)
    print(fixed_rules)
    fixed_update = []
    fixes = {}
    for idx, page in enumerate(update):
        fixed_index = get_index(page, fixed_rules)
        fixes[page] = {"initial_index": idx, "fixed_index": fixed_index}
    print(fixes)

    return fixed_update


def fix_the_invalid_updates(updates, rules):
    valid_updates = []
    for update in updates:
        print(update)
        invalid_rules = find_broken_rules(update, rules)
        print(invalid_rules)
        fixed = fix_update(update, invalid_rules)
        print(fixed)
    print(valid_updates)


if __name__ == "__main__":
    input_name = "sample.txt"
    rules, updates = read_input(input_name)
    invalid_updates = find_valid_updates(updates, rules)
    fix_the_invalid_updates(invalid_updates, rules)
