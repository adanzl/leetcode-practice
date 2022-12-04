def main():
    n, m, q = map(int, input().split())
    w = [int(x) for x in input().split()]

    #-------- 每种state对应的权重和
    state_wSum = [0 for _ in range(1 << n)]
    for state in range(1 << n):
        for i in range(n):
            if (state >> i) & 1:
                state_wSum[state] += w[i]

    #-------- 将每个字符串，压缩成一个整数。
    xf = [0 for _ in range(1 << n)]
    for _ in range(m):
        s = input()
        x = 0
        for i in range(n - 1, -1, -1):
            x = x * 2 + (ord(s[i]) - ord('0'))
            # x = x * 2 + int(s[i])
        xf[x] += 1

    #-------- state匹配state
    cnt = [[0 for _ in range(101)] for _ in range(1 << n)]
    mask = (1 << n) - 1
    for x in range(1 << n):
        for y in range(1 << n):
            cur = state_wSum[x ^ y ^ mask]
            if cur <= 100:
                cnt[x][cur] += xf[y]

    #-------- cnt前缀和数组
    for i in range(1 << n):
        for j in range(1, 101):
            cnt[i][j] += cnt[i][j - 1]

    for _ in range(q):
        t, k = input().split()
        k = int(k)

        x = 0
        for i in range(n - 1, -1, -1):
            x = x * 2 + (ord(t[i]) - ord('0'))
        cur = cnt[x][k]
        print(cur)


if __name__ == '__main__':
    main()
