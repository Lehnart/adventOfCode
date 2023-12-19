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
                characteristic = characteristic.replace("{","").replace("}","")
                operation = "gt"
            elif "<" in raw_key:
                characteristic, value = raw_key.split("<")
                characteristic = characteristic.replace("{","").replace("}","")
                operation = "lt"
            else:
                raise Exception
            rules[name].append((characteristic, operation, int(value), destination))

        else:
            rules[name].append((None, None, None, condition_map))

elements = []
for raw_elements in lines[571:]:
    element_dict = {}
    for raw_element in raw_elements.replace("{","").replace("}","").split(","):
        characteristic, value = raw_element.split("=")
        element_dict[characteristic] = int(value)
    elements.append(element_dict)

accepteds = []
for element in elements :
    next_rule = "in"
    while next_rule != "R" and next_rule != "A" :
        rule = rules[next_rule]
        for condition in rule :
            if condition[0] is None :
                next_rule = condition[3]
                break
            elif condition[1] == "gt" and element[condition[0]] > condition[2]:
                next_rule = condition[3]
                break
            elif condition[1] == "lt" and element[condition[0]] < condition[2]:
                next_rule = condition[3]
                break
    if next_rule == "A":
        accepteds.append(element)
somme = 0
for accept in accepteds :
    for c in "xmas" :
        somme += accept[c]
