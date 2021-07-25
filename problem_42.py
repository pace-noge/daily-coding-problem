#!/bin/python3

"""
Given a list of integer s and target number k, write a function that return
a subset of s that add up to k. if such a subset cannot be mad, then return
null

integers can appear more than twice in the list. You may assume all numbers in
the list are positive.

For example:
given S = [12, 1, 61, 5, 9, 2] and k = 24
return [12, 9, 2, 1] since it sums up to 24.

"""

from typing import List


def adds_up_to(s: List[int], k: int):
    s = list(filter(lambda x: x < k, s))
    s.sort(reverse=True)
    subs = []
    for i in range(len(s)):

        if sum(subs + [s[i]]) < k:            subs.append(s[i])
        elif sum(subs + [s[i]]) > k:
            continue
        elif sum(subs + [s[i]]) == k:
            subs.append(s[i])
            return subs
    return None

if __name__ == "__main__":
    s = [12, 1, 61, 5, 9, 2]
    k = 24
    print(adds_up_to(s, k))


