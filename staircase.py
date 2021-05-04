

n = int(input(''))
if 0 < n and n <= 100:
    for i in range(0, n):
        print(' '*(n-i-1) + (i+1)*'#')
else:
    print('nope')
