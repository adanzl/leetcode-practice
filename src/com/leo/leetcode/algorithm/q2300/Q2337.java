package com.leo.leetcode.algorithm.q2300;

import com.leo.utils.TestCase;

/**
 * 给你两个字符串 start 和 target ，长度均为 n 。每个字符串 仅 由字符 'L'、'R' 和 '_' 组成，其中：
 * 1、字符 'L' 和 'R' 表示片段，其中片段 'L' 只有在其左侧直接存在一个 空位 时才能向 左 移动，而片段 'R' 只有在其右侧直接存在一个 空位 时才能向 右 移动。
 * 2、字符 '_' 表示可以被 任意 'L' 或 'R' 片段占据的空位。
 * 如果在移动字符串 start 中的片段任意次之后可以得到字符串 target ，返回 true ；否则，返回 false 。
 * 提示：
 * 1、n == start.length == target.length
 * 2、1 <= n <= 10^5
 * 3、start 和 target 由字符 'L'、'R' 和 '_' 组成
 * 链接：https://leetcode.cn/problems/move-pieces-to-obtain-a-string
 */
public class Q2337 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q2337().canChange("R___LR_", "__RL__R"));
        // true
        System.out.println(new Q2337().canChange("__LL", "LL__"));
        TestCase tc1 = new TestCase("resources/algorithm/q2300/Q2337/Case1.txt");
        // true
        System.out.println(new Q2337().canChange(tc1.getData(0), tc1.getData(1)));
        TestCase tc2 = new TestCase("resources/algorithm/q2300/Q2337/Case2.txt");
        // true
        System.out.println(new Q2337().canChange(tc1.getData(0), tc1.getData(1)));
        // false
        System.out.println(new Q2337().canChange("____", "R_RR"));
        // false
        System.out.println(new Q2337().canChange("_R", "R_"));
        // true
        System.out.println(new Q2337().canChange("_L__R__R_", "L______RR"));
        // false
        System.out.println(new Q2337().canChange("R_L_", "__LR"));
    }

    public boolean canChange(String start, String target) {
        int n = start.length();
        char[] s = start.toCharArray(), t = target.toCharArray();
        String sStr = start.replaceAll("_", ""), tStr = target.replaceAll("_", "");
        if (!sStr.equals(tStr)) return false;
        int sr = 0, sl = 0, tr = 0, tl = 0;
        for (int i = 0; i < n; i++) {
            if (t[i] == 'R') tr++;
            else if (t[i] == 'L') tl++;
            if (s[i] == 'R') sr++;
            else if (s[i] == 'L') sl++;
            if (tr > sr || tl < sl) return false;
        }
        return true;
    }
}
