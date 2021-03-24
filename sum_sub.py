
def is_sum_sub(arr, k):
    for i in range(len(arr)):
        if arr[i] < k:
            x = k-arr[i]
            if x in arr:
                return True
    return False


if __name__ == "__main__":
    arr = [10, 15, 3, 7]
    k = 17
    print(is_sum_sub(arr, k))
    arr = [20, 1, 3, 5]
    k = 7
    print(is_sum_sub(arr, k))


