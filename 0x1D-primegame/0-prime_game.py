#!/usr/bin/python3
"""prime game"""


def isWinner(x, nums):
    """Solve"""
    if not nums or x < 1:
        return None
    n = max(nums)
    sift = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not sift[i]:
            continue
        for j in range(i*i, n + 1, i):
            sift[j] = False

    sift[0] = sift[1] = False
    c = 0
    for i in range(len(sift)):
        if sift[i]:
            c += 1
        sift[i] = c

    player1 = 0
    for n in nums:
        player1 += sift[n] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
