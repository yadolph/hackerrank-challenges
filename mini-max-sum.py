

n = list(map(int, input().rstrip().split()))
n.sort()

max_sum = sum(n[1:5])
min_sum = sum(n[0:4])

print(min_sum, max_sum)
