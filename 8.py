s = list(map(int, input().split(" ")))

res = 1

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        res+=1
print(res)
