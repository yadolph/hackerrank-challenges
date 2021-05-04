

if __name__ == '__main__':
    _, int_list = input(''), list(map(int, input().rstrip().split()))
    print(sum(int_list))
