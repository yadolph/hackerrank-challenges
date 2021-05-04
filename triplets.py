

def compareTriplets(a, b):
    if len(a) != len(b):
        print('Something is wrong, I can feel it')
    result = [0,0]
    for idx, val in enumerate(a):
        if a[idx] == b[idx]:
            continue
        elif a[idx] > b[idx]:
            result[0] += 1
        elif a[idx] < b[idx]:
            result[1] += 1
    return result


if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)

    print(f'{result[0]} {result[1]}')
