from collections import deque

t = int(input())
answer = []
for i in range(t):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))

    q = deque((i, v) for i, v in enumerate(docs))  # (문서 위치, 중요도)
    docs.sort(reverse=True)  # 내림차순

    cnt = 0
    while True:
        cur = q.popleft()  # 현재 가장 앞에 있는 문서
        if cur[1] == docs[0]:  # 현재 문서가 중요도 제일 높을 때
            cnt += 1
            docs.pop(0)
            if cur[0] == m:
                answer.append(cnt)
                break
        else:
            q.append(cur)
    print(answer[i])
