
def my_solution(arr):
    ret = []
    for i in range(len(arr)):
        t = 1
        for j in range(len(arr)):
            if i == j:
                continue
            t *= j
        ret.append(j)
    return ret


if __name__ == "__main__":
    test = [1, 2, 3]
    print(my_solution(test))
