package com.leo.leetcode.algorithm.q1600;


import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 我们有 n 栋楼，编号从 0 到 n - 1 。每栋楼有若干员工。由于现在是换楼的季节，部分员工想要换一栋楼居住。
 * 给你一个数组 requests ，其中 requests[i] = [from_i, to_i] ，表示一个员工请求从编号为 from_i 的楼搬到编号为 to_i 的楼。
 * 一开始 所有楼都是满的，所以从请求列表中选出的若干个请求是可行的需要满足 每栋楼员工净变化为 0 。
 * 意思是每栋楼 离开 的员工数目 等于 该楼 搬入 的员工数数目。
 * 比方说 n = 3 且两个员工要离开楼 0 ，一个员工要离开楼 1 ，一个员工要离开楼 2 ，如果该请求列表可行，
 * 应该要有两个员工搬入楼 0 ，一个员工搬入楼 1 ，一个员工搬入楼 2 。
 * 请你从原请求列表中选出若干个请求，使得它们是一个可行的请求列表，并返回所有可行列表中最大请求数目。
 * 提示：
 * 1、1 <= n <= 20
 * 2、1 <= requests.length <= 16
 * 3、requests[i].length == 2
 * 4、0 <= from_i, to_i < n
 * 链接：https://leetcode-cn.com/problems/maximum-number-of-achievable-transfer-requests
 */
public class Q1601 {

    public static void main(String[] args) {
        // 3
//        System.out.println(new Q1601().maximumRequests(5, stringToInt2dArray("[[2,0],[3,0],[4,2],[4,1],[0,1],[1,2],[3,1],[3,0],[1,2]]")));
        // 0
        System.out.println(new Q1601().maximumRequests(4, stringToInt2dArray("[[3,0],[3,0],[0,1],[1,2],[3,2],[1,2]]")));
        // 4
        System.out.println(new Q1601().maximumRequests(3, stringToInt2dArray("[[1,2],[1,2],[2,2],[0,2],[2,1],[1,1],[1,2]]")));
        // 0
        System.out.println(new Q1601().maximumRequests(3, stringToInt2dArray("[[2,0],[2,1],[0,1],[0,1]]")));
        // 2
        System.out.println(new Q1601().maximumRequests(3, stringToInt2dArray("[[1,2],[1,2],[0,2],[2,1]]")));
        // 1
        System.out.println(new Q1601().maximumRequests(1, stringToInt2dArray("[[0,0]]")));
        // 5
        System.out.println(new Q1601().maximumRequests(5, stringToInt2dArray("[[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]")));
        // 3
        System.out.println(new Q1601().maximumRequests(3, stringToInt2dArray("[[0,0],[1,2],[2,1]]")));
        // 4
        System.out.println(new Q1601().maximumRequests(5, stringToInt2dArray("[[0,3],[3,1],[1,2],[2,0]]")));
    }

    int ret = 0;
    int[][] requests;

    public int maximumRequests(int n, int[][] requests) {
        this.requests = requests;
        walk(0, 0, new int[n]);
        return ret;
    }

    void walk(int sum, int idx, int[] mark) {
        boolean fit = true;
        for (int m : mark)
            if (m != 0) {
                fit = false;
                break;
            }
        if (fit) ret = Math.max(ret, sum);
        if (idx == requests.length) return;
        int[] request = requests[idx];
        mark[request[0]]--;
        mark[request[1]]++;
        walk(sum + 1, idx + 1, mark);
        mark[request[0]]++;
        mark[request[1]]--;
        walk(sum, idx + 1, mark);
    }
}
