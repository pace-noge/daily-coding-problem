

def longest_consecutive(elements: list) -> int:
    # sort the elements
    elements = sorted(elements)
    count = 1
    ans = 0
    for i in range(1, len(elements)):
        if elements[i] == elements[i-1] + 1:
            count += 1
        else:
            count = 1
        ans = max([ans, count])
    return ans



if __name__ == "__main__":
    t = [100, 4, 200, 1, 3, 2]
    ret = longest_consecutive(t)
    print(ret)
    assert(longest_consecutive(t) == 4)



