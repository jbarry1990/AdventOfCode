
def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        index = content.index("\n")
        page_rules = content[0:index]
        page_order = content[index+1:]
        page_rules=[x.strip() for x in page_rules]
        page_order=[x.strip() for x in page_order]
        return page_rules, page_order
        
    


def PartASolve(page_rules, page_order):
    rules = []
    orders = []
    incorrect = []
    total = 0
    for rule in page_rules:
        rules.append([int(x) for x in rule.split("|")])

    orders = [x.split(",") for x in page_order]
    orders = [[int(x) for x in y] for y in orders]

    for order in orders:
        for rule in rules:
            if rule[0] in order and rule[1] in order:
                if order.index(rule[0]) > order.index(rule[1]):
                    incorrect.append(order)
                    break
        else:
            total += order[len(order)//2]

    return total, incorrect, rules

def PartBSolve(incorrect,rules):
    total = 0
    for datum in incorrect:
        good = False
        while good == False:
            good = True
            for rule in rules:
                if rule[0] in datum and rule[1] in datum:
                    a = datum.index(rule[0])
                    b = datum.index(rule[1])
                    if a > b:
                        datum[a],datum[b] = datum[b],datum[a]
                        good = False
        total += datum[len(datum)//2]

    return total

def main():
    page_rules, page_order = ReadFile("Inputs.txt")
    answer, incorrect,rules = PartASolve(page_rules, page_order)
    print("Part A Answer: ", answer)
    answer = PartBSolve(incorrect,rules)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
