import sys
arr = [list(sys.stdin.readline().split()) for _ in range(20)]
grade = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
total = 0
score = 0
for i in arr:
    if i[2] == 'P':
        i[1] = 0
    total += float(i[1])
    for key in grade:
        if key == i[2]:
            score += float(i[1]) * grade[key]
            
print(score/total)