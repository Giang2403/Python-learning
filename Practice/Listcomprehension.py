
K = int(input())
lst = list(map(int, input().split()))
s = set(lst)
for i in s:
    if lst.count(i) == 1:
        print(i)
        break