package com.leo.leetcode.algorithm.q0600;

import static com.leo.utils.LCUtil.stringToStringArray;

/**
 * 你现在是一场采用特殊赛制棒球比赛的记录员。这场比赛由若干回合组成，过去几回合的得分可能会影响以后几回合的得分。
 * 比赛开始时，记录是空白的。你会得到一个记录操作的字符串列表 ops，其中 ops[i] 是你需要记录的第 i 项操作，ops 遵循下述规则：
 * 1、整数 x - 表示本回合新获得分数 x
 * 2、"+" - 表示本回合新获得的得分是前两次得分的总和。题目数据保证记录此操作时前面总是存在两个有效的分数。
 * 3、"D" - 表示本回合新获得的得分是前一次得分的两倍。题目数据保证记录此操作时前面总是存在一个有效的分数。
 * 4、"C" - 表示前一次得分无效，将其从记录中移除。题目数据保证记录此操作时前面总是存在一个有效的分数。
 * 请你返回记录中所有得分的总和。
 * 提示：
 * 1、1 <= ops.length <= 1000
 * 2、ops[i] 为 "C"、"D"、"+"，或者一个表示整数的字符串。整数范围是 [-3 * 10^4, 3 * 10^4]
 * 3、对于 "+" 操作，题目数据保证记录此操作时前面总是存在两个有效的分数
 * 4、对于 "C" 和 "D" 操作，题目数据保证记录此操作时前面总是存在一个有效的分数
 * 链接：https://leetcode-cn.com/problems/baseball-game
 */
public class Q682 {

    public static void main(String[] args) {
        // 30
        System.out.println(new Q682().calPoints(stringToStringArray("[\"5\",\"2\",\"C\",\"D\",\"+\"]")));
        // 27
        System.out.println(new Q682().calPoints(stringToStringArray("[\"5\",\"-2\",\"4\",\"C\",\"D\",\"9\",\"+\",\"+\"]")));
        // 1
        System.out.println(new Q682().calPoints(stringToStringArray("[\"1\"]")));
    }

    public int calPoints(String[] ops) {
        int ret = 0, s = 0;
        int[] stack = new int[1000];
        for (String op : ops) {
            if ("C".equals(op)) {
                ret -= stack[--s];
            } else if ("D".equals(op)) {
                int score = stack[s - 1] * 2;
                stack[s++] = score;
                ret += stack[s - 1];
            } else if ("+".equals(op)) {
                int score = stack[s - 1] + stack[s - 2];
                ret += score;
                stack[s++] = score;
            } else {
                stack[s++] = Integer.parseInt(op);
                ret += stack[s - 1];
            }
        }
        return ret;
    }
}
