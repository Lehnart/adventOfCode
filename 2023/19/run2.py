import copy
from interval import interval, inf, imath

with open("input.txt") as file:
    lines = file.readlines()

rules = {}
for rule in lines[:570]:
    name = rule[:rule.find("{")]
    rules[name] = []
    condition_maps = rule[rule.find("{"):rule.find("}")].split(",")
    for condition_map in condition_maps:
        if ":" in condition_map:
            raw_key, destination = condition_map.split(":")
            if ">" in raw_key:
                characteristic, value = raw_key.split(">")
                characteristic = characteristic.replace("{", "").replace("}", "")
                operation = "gt"
            elif "<" in raw_key:
                characteristic, value = raw_key.split("<")
                characteristic = characteristic.replace("{", "").replace("}", "")
                operation = "lt"
            else:
                raise Exception
            rules[name].append((characteristic, operation, int(value), destination))

        else:
            rules[name].append((None, None, None, condition_map))

rules_to_A = []
for rule in rules:
    conditions = rules[rule]
    for condition in conditions:
        if condition[3] == "A":
            rules_to_A.append(rule)
            break

next_rules_to_visit = [{"A": 0}]
next_next_rules = []
starting_from_in = []
while next_rules_to_visit:
    for rule_to_visit in next_rules_to_visit:
        rule_key_to_visit = list(rule_to_visit.keys())[0]
        if rule_key_to_visit == "in":
            starting_from_in.append(copy.deepcopy(rule_to_visit))
            continue
        for rule_key in rules:
            conditions = rules[rule_key]
            for condition in conditions:
                if condition[3] == rule_key_to_visit:
                    new_dict = {rule_key: rule_to_visit}
                    next_next_rules.append(new_dict)
                    break
    next_rules_to_visit = copy.deepcopy(next_next_rules)
    next_next_rules = []

all_conditions_to_A = []
for path in starting_from_in:
    conditions_to_A = []
    key = list(path.keys())[0]
    while key != "A":
        dest = list(path[key].keys())[0]
        for condition in rules[key]:
            if condition[3] == dest:
                if condition[0] is not None :
                    conditions_to_A.append(condition[:3])
                break
            else:
                conditions_to_A.append((condition[0], "gte" if condition[1] == "lt" else "lte", condition[2]))
        path = path[key]
        key = dest
    all_conditions_to_A.append(conditions_to_A)
for condition in all_conditions_to_A :
    print(condition)
