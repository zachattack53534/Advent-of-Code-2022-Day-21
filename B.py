def find_answer(start, equation, target, previous, index):
    _target = round(eval(target))
    _value = round(eval(equation.format(int("".join(start)))))

    if _target == _value:
        return int("".join(start))
    if _target - _value < 0:
        start = previous
        index += 1
    if _target - _value > 0:
        previous = start[:]
        if start[index] == "0":
            index += 1
        start[index] = str(int(start[index]) - 1)

    return find_answer(start, equation, target, previous, index)



def find_humn(current, dict):
    if current == "humn":
        return True
    if dict[current].isnumeric():
        pass
    else:
        moves = dict[current].split(" ")
        first = find_humn(moves[0], dict)
        second = find_humn(moves[2], dict)

        if first or second:
            return True
        else:
            return False


def dfs(current, dict):
    if dict[current].isnumeric():
        return dict[current]
    else:
        equation = dict[current].split(" ")
        first = equation[0]
        second = equation[2]
        if first != "humn":
            first = dfs(first, dict)
        else:
            first = "{}}"
        if second != "humn":
            second = dfs(second, dict)
        else:
            second = "{}"

        operation = equation[1]

        return f"({first} {operation} {second})"


def calculate(dict):
    moves = dict["root"].split(" ")
    first = moves[0]
    second = moves[2]

    first = dfs(first, dict)
    second = dfs(second, dict)

    if find_humn(moves[0], dict):
        return find_answer(list("9999999999999999"), first, second, list("9999999999999999"), 0)
