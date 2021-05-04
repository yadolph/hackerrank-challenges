

def matrix_assemble():
    _, first_line = input(''), input('')
    f_line_lst = list(map(int, first_line.rstrip().split()))
    matrix = []
    matrix.append(f_line_lst)
    for i in range(0, len(f_line_lst)-1):
        lst = list(map(int, input('').rstrip().split()))
        matrix.append(lst)
    return matrix


def count_diags(matrix):
    pr_diag = 0
    sec_diag = 0
    for idx, val in enumerate(matrix):
        pr_diag += val[idx]
        sec_diag += val[-1-idx]
    return pr_diag, sec_diag


if __name__ == '__main__':
    matrix = matrix_assemble()
    a, b = count_diags(matrix)
    print(abs(a-b))
