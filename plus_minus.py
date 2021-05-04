

def count_ratios(array):
    pos = 0
    neg = 0
    zer = 0
    for item in array:
        if item == 0:
            zer += 1
        elif item < 0:
            neg += 1
        else:
            pos += 1
    ratio_sum = pos + neg + zer
    pos_ratio = pos / ratio_sum
    neg_ratio = neg / ratio_sum
    zer_ratio = zer / ratio_sum
    return pos_ratio, neg_ratio, zer_ratio


_, array = input(''), list(map(int, input('').rstrip().split()))

ratios = count_ratios(array)
for item in ratios:
    print('{:.6f}'.format(round(item, 6)))
