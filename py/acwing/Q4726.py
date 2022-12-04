"""
 * 链接：https://www.acwing.com/problem/content/4729/
"""
# 下一个排列
def nextPermutation(nums):
    n = len(nums)
    idx = len(nums) - 1
    while idx >= 0:
        if nums[idx] > nums[idx - 1]:
            break
        idx -= 1
    if idx == 0:
        nums[:] = nums[::-1]
        return nums
    j = n - 1
    while j >= 0:
        if nums[j] > nums[idx - 1]:
            break
        j -= 1

    nums[idx - 1], nums[j] = nums[j], nums[idx - 1]
    nums[idx:] = nums[idx:][::-1]
    return nums


def solve1():
    n = input()
    l = len(n)
    num = int(n)
    if l & 1:
        print("".join(['4'] * ((l + 1) // 2) + ['7'] * ((l + 1) // 2)))
    else:
        c4, c7 = l // 2, l // 2
        if num > int('7' * c7 + '4' * c4):
            print("".join(['4'] * (c4 + 1) + ['7'] * (c7 + 1)))
            exit()
        ans = ['4'] * (c4) + ['7'] * (c7)
        nn = list(n)
        while ans < nn:
            ans = nextPermutation(ans)

        print("".join(ans))


def solve2():

    def dfs(s, c4, c7, n):
        if c4 == 0 and c7 == 0 and s >= n:
            return s
        ret = None
        if c4:
            ret = dfs(s + '4', c4 - 1, c7, n)
            if ret: return ret
        if c7:
            ret = dfs(s + '7', c4, c7 - 1, n)
            if ret: return ret
        return None

    n = '4777'
    # n = input()
    l = len(n)
    if l & 1:
        print("".join(['4'] * ((l + 1) // 2) + ['7'] * ((l + 1) // 2)))
    else:
        if n > '7' * (l // 2) + '4' * (l // 2):
            print('4' * (l // 2 + 1) + '7' * (l // 2 + 1))
        else:
            print(dfs("", l // 2, l // 2, n))


# solve1()
solve2()