
def is_sum_sub(arr, k):
    for i in range(len(arr[0])):
        t = k - arr[0][i]
        if t in arr[1]:
            return True
    return False



if __name__ == "__main__":
    test_arr = [[1, 3, 4, 5, 7], [2, 20, 15, 6]]
    k = 5
    print(is_sum_sub(test_arr, k))
    k = 30
    print(is_sum_sub(test_arr, k))
