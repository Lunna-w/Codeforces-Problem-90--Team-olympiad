team = []

programmers = []
mathematicians = []
pe = []

n = int(input())

p = list(map(int, input().split()))

for i, student in enumerate(p):
    if student == 1:
        programmers.append(i + 1) 
    elif student == 2:
        mathematicians.append(i + 1)
    elif student == 3:
        pe.append(i + 1)

while programmers and mathematicians and pe:
    team.append([programmers.pop(), mathematicians.pop(), pe.pop()])

print(len(team))
for members in team:
    print(*members)

