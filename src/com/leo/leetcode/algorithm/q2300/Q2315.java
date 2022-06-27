package com.leo.leetcode.algorithm.q2300;

/**
 * 给你一个字符串 s ，每 两个 连续竖线 '|' 为 一对 。换言之，第一个和第二个 '|' 为一对，第三个和第四个 '|' 为一对，以此类推。
 * 请你返回 不在 竖线对之间，s 中 '*' 的数目。
 * 注意，每个竖线 '|' 都会 恰好 属于一个对。
 * 提示：
 * 1、1 <= s.length <= 1000
 * 2、s 只包含小写英文字母，竖线 '|' 和星号 '*' 。
 * 3、s 包含 偶数 个竖线 '|' 。
 * 链接：https://leetcode.cn/problems/count-asterisks
 */
public class Q2315 {

    public static void main(String[] args) {
        // 2
        System.out.println(new Q2315().countAsterisks("l|*e*et|c**o|*de|"));
        // 0
        System.out.println(new Q2315().countAsterisks("iamprogrammer"));
        // 5
        System.out.println(new Q2315().countAsterisks("yo|uar|e**|b|e***au|tifu|l"));
    }

    public int countAsterisks(String s) {
        char[] str = s.toCharArray();
        int ret = 0, cnt = 0;
        for (char c : str) {
            if (c == '|') cnt++;
            if (c == '*') {
                if ((cnt & 1) == 0) ret++;
            }
        }
        return ret;
    }

}
