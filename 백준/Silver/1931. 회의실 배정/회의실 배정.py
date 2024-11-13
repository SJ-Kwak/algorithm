import sys
input = sys.stdin.readline

n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]

def solution(n, meetings):
    answer = 0
    meetings.sort(key=lambda x: (x[1], x[0]))
    endTime = 0
    for start, end in meetings:
        if start >= endTime:
            endTime = end
            answer += 1
    return answer

print(solution(n, meetings))