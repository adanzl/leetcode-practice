package com.leo.leetcode.algorithm.q2000;

import com.leo.utils.TestCase;

import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给你一棵根节点为 0 的 二叉树 ，它总共有 n 个节点，节点编号为 0 到 n - 1 。
 * 同时给你一个下标从 0 开始的整数数组 parents 表示这棵树，其中 parents[i] 是节点 i 的父节点。由于节点 0 是根，所以 parents[0] == -1 。
 * 一个子树的 大小 为这个子树内节点的数目。每个节点都有一个与之关联的 分数 。
 * 求出某个节点分数的方法是，将这个节点和与它相连的边全部 删除 ，剩余部分是若干个 非空 子树，这个节点的 分数 为所有这些子树 大小的乘积 。
 * 请你返回有 最高得分 节点的 数目 。
 * 提示：
 * 1、n == parents.length
 * 2、2 <= n <= 10^5
 * 3、parents[0] == -1
 * 4、对于 i != 0 ，有 0 <= parents[i] <= n - 1
 * 5、parents 表示一棵二叉树。
 * 链接：https://leetcode-cn.com/problems/count-nodes-with-the-highest-score
 */
public class Q2049 {

    public static void main(String[] args) {
        // 1
        TestCase tc = new TestCase("resources/algorithm/q2000/Q2049/Case001.txt");
        System.out.println(new Q2049().countHighestScoreNodes(stringToIntegerArray(tc.getData(0))));
        // 3
        System.out.println(new Q2049().countHighestScoreNodes(stringToIntegerArray("[-1,2,0,2,0]")));
        // 2
        System.out.println(new Q2049().countHighestScoreNodes(stringToIntegerArray("[-1,2,0]")));
    }

    public int countHighestScoreNodes(int[] parents) {
        int len = parents.length, ret = -1;
        long max = 0;
        int[][] map = new int[len][]; // [0]root-[1]size-[2]left-[3]right
        for (int i = 0; i < len; i++) map[i] = new int[]{i, 1, -1, -1};
        for (int i = 0; i < len; i++) {
            int parent = parents[i];
            if (parent == -1) {
                map[i][0] = i;
                continue;
            }
            map[i][0] = parent;
            // add to parent node
            if (map[parent][2] == -1) map[parent][2] = i;
            else map[parent][3] = i;
            int idx = i;
            while (idx != map[idx][0]) {
                int lSize = map[parent][2] == -1 ? 0 : map[map[parent][2]][1];
                int rSize = map[parent][3] == -1 ? 0 : map[map[parent][3]][1];
                map[parent][1] = lSize + rSize + 1;
                map[idx][0] = parent;
                idx = parent;
                parent = map[idx][0];
            }
        }
        for (int i = 0; i < len; i++) {
            long n1 = map[i][2] == -1 ? 1 : map[map[i][2]][1];
            long n2 = map[i][3] == -1 ? 1 : map[map[i][3]][1];
            long n3 = getRootSize(map, i) - map[i][1];
            long n = Math.max(n1, 1) * Math.max(n2, 1) * Math.max(n3, 1);
            if (n > max) {
                max = n;
                ret = 1;
            } else if (n == max) {
                ret++;
            }
        }
        return ret;
    }

    int getRootSize(int[][] map, int idx) {
        int i = idx, parent = map[i][0];
        while (parent != i) {
            i = parent;
            parent = map[i][0];
        }
        map[idx][0] = parent;
        return map[parent][1];
    }

}
