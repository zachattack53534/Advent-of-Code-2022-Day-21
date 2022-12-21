import A
import B

with open("input.txt", "r") as file:
    data = file.read().strip().split("\n")

dict = {}
for line in data:
    line = line.split(": ")
    dict[line[0]] = line[1]

print(f"The answer to part A is: {A.calculate(dict)}")
print(f"The answer to part B is: {B.calculate(dict)}")
