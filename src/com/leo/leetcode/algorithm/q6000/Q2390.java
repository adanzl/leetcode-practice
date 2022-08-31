package com.leo.leetcode.algorithm.q6000;

/**
 * 给你一个包含若干星号 * 的字符串 s 。
 * 在一步操作中，你可以：
 * 1、选中 s 中的一个星号。
 * 2、移除星号 左侧 最近的那个 非星号 字符，并移除该星号自身。
 * 返回移除 所有 星号之后的字符串。
 * 注意：
 * 1、生成的输入保证总是可以执行题面中描述的操作。
 * 2、可以证明结果字符串是唯一的。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 由小写英文字母和星号 * 组成
 * 3、s 可以执行上述操作
 * 链接：https://leetcode.cn/problems/removing-stars-from-a-string
 */
public class Q2390 {

    public static void main(String[] args) {
        // "lecoe"
        System.out.println(new Q2390().removeStars("leet**cod*e"));
        // ""
        System.out.println(new Q2390().removeStars("erase*****"));
    }

    public String removeStars(String s) {
        int n = s.length(), nz = 0;
        StringBuilder ans = new StringBuilder();
        for (int i = n - 1; i >= 0; i--) {
            if (s.charAt(i) == '*') nz++;
            else {
                if (nz == 0) ans.insert(0, s.charAt(i));
                else nz--;
            }
        }
        return ans.toString();
    }

}
