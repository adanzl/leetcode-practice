package com.leo.leetcode.algorithm.q0500;

import java.util.*;

/**
 * 电子游戏“辐射4”中，任务 “通向自由” 要求玩家到达名为 “Freedom Trail Ring” 的金属表盘，并使用表盘拼写特定关键词才能开门。
 * 给定一个字符串 ring ，表示刻在外环上的编码；给定另一个字符串 key ，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的最少步数。
 * 最初，ring 的第一个字符与 12:00 方向对齐。您需要顺时针或逆时针旋转 ring 以使 key 的一个字符在 12:00 方向对齐，然后按下中心按钮，以此逐个拼写完 key 中的所有字符。
 * 旋转 ring 拼出 key 字符 key[i] 的阶段中：
 * 1、您可以将 ring 顺时针或逆时针旋转 一个位置 ，计为1步。旋转的最终目的是将字符串 ring 的一个字符与 12:00 方向对齐，并且这个字符必须等于字符 key[i] 。
 * 2、如果字符 key[i] 已经对齐到12:00方向，您需要按下中心按钮进行拼写，这也将算作 1 步。按完之后，您可以开始拼写 key 的下一个字符（下一阶段）, 直至完成所有拼写。
 * 提示：
 * 1、1 <= ring.length, key.length <= 100
 * 2、ring 和 key 只包含小写英文字母
 * 3、保证 字符串 key 一定可以由字符串  ring 旋转拼出
 * 链接：https://leetcode.cn/problems/freedom-trail
 */
public class Q514 {

    public static void main(String[] args) {
        // 13
        System.out.println(new Q514().findRotateSteps("godding", "godding"));
        // 4
        System.out.println(new Q514().findRotateSteps("godding", "gd"));
    }

    public int findRotateSteps(String ring, String key) {
        char[] rStr = ring.toCharArray(), kStr = key.toCharArray();
        int n = rStr.length, ret = Integer.MAX_VALUE;
        List<List<Integer>> cMap = new ArrayList<>(26);
        for (int i = 0; i < 26; i++) cMap.add(new ArrayList<>());
        for (int i = 0; i < n; i++) cMap.get(rStr[i] - 'a').add(i);
        int[][] pos = new int[][]{{0, 0}}; // len-idx
        for (char k : kStr) {
            List<Integer> nextIdx = cMap.get(k - 'a');
            int[][] nextPos = new int[nextIdx.size()][];
            for (int i = 0; i < nextIdx.size(); i++) {
                int next = nextIdx.get(i);
                nextPos[i] = new int[]{0x3f3f3f3f, next};
                for (int[] po : pos) {
                    int idx1 = Math.max(po[1], next), idx2 = Math.min(po[1], next);
                    int dist = idx1 == idx2 ? 1 : (Math.min(idx1 - idx2, idx2 + n - idx1) + 1);
                    int v = po[0] + dist; // pos[i][0]-next
                    nextPos[i][0] = Math.min(nextPos[i][0], v);
                }
            }
            pos = nextPos;
        }
        for (int[] p : pos) ret = Math.min(ret, p[0]);
        return ret;
    }
}
