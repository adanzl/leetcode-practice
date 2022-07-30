package com.leo.leetcode.algorithm.q0900;

import java.util.ArrayList;
import java.util.List;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个由不同正整数的组成的非空数组 nums ，考虑下面的图：
 * 1、有 nums.length 个节点，按从 nums[0] 到 nums[nums.length - 1] 标记；
 * 2、只有当 nums[i] 和 nums[j] 共用一个大于 1 的公因数时，nums[i] 和 nums[j]之间才有一条边。
 * 返回 图中最大连通组件的大小 。
 * 提示：
 * 1、1 <= nums.length <= 2 * 10^4
 * 2、1 <= nums[i] <= 10^5
 * 3、nums 中所有值都 不同
 * 链接：https://leetcode.cn/problems/largest-component-size-by-common-factor
 */
public class Q952 {

    public static void main(String[] args) {
        // 5
        System.out.println(new Q952().largestComponentSize(stringToIntegerArray("[1,4,6,15,35]")));
        // 4
        System.out.println(new Q952().largestComponentSize(stringToIntegerArray("[4,6,15,35]")));
        // 8
        System.out.println(new Q952().largestComponentSize(stringToIntegerArray("[2,3,6,7,4,12,21,39]")));
        // 2
        System.out.println(new Q952().largestComponentSize(stringToIntegerArray("[20,50,9,63]")));
    }

    int[][] parent;

    public int largestComponentSize(int[] nums) {
        int ret = 1;
        parent = new int[100001][];
        for (int i = 0; i < parent.length; i++) parent[i] = new int[]{i, 0};
        for (int num : nums) {
            if (num == 1) continue;
            int p = 2;
            List<Integer> pList = new ArrayList<>();
            while (p * p <= num) {
                if (num % p == 0) {
                    while (num % p == 0) num /= p;
                    pList.add(p);
                } else p++;
            }
            if (num > 1) pList.add(num);
            for (int i = 1; i < pList.size(); i++) merge(pList.get(i - 1), pList.get(i));
            ret = Math.max(ret, ++parent[find(pList.get(0))][1]);
        }
        return ret;
    }

    int find(int x) {
        return parent[x][0] == x ? x : (parent[x][0] = find(parent[x][0]));
    }

    void merge(int i0, int i1) {
        int r0 = find(i0), r1 = find(i1);
        if (r0 == r1) return;
        parent[r1][0] = r0;
        parent[r0][1] += parent[r1][1];
    }
}
