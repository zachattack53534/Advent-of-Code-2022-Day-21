def dfs(current, dict):
    if dict[current].isnumeric():
        return dict[current]
    else:
        equation = dict[current].split(" ")
        first = dfs(equation[0], dict)
        second = dfs(equation[2], dict)
        operation = equation[1]

        return eval(f"{first} {operation} {second}")


def calculate(dict):
    target = "root"
    equation = dict[target].split(" ")
    first = dfs(equation[0], dict)
    second = dfs(equation[2], dict)
    operation = equation[1]

    return round(eval(f"{first} {operation} {second}"))
