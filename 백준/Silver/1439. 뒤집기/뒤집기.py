import sys
s = sys.stdin.readline().strip()

def solution(s):
  zero = 0
  one = 0

  if s[0] == '1':
    zero += 1
  else:
    one += 1
  
  for i in range(len(s)-1):
    if s[i] != s[i+1]:
      if s[i+1] == '1':
        zero += 1
      else:
        one += 1
  
  return min(zero, one)

print(solution(s))