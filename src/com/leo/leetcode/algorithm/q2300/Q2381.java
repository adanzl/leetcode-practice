package com.leo.leetcode.algorithm.q2300;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给你一个小写英文字母组成的字符串 s 和一个二维整数数组 shifts ，其中 shifts[i] = [start_i, end_i, direction_i] 。
 * 对于每个 i ，将 s 中从下标 start_i 到下标  end_i （两者都包含）所有字符都进行移位运算，如果 direction_i = 1 将字符向后移位，如果 direction_i = 0 将字符向前移位。
 * 将一个字符 向后 移位的意思是将这个字符用字母表中 下一个 字母替换（字母表视为环绕的，所以 'z' 变成 'a'）。
 * 类似的，将一个字符 向前 移位的意思是将这个字符用字母表中 前一个 字母替换（字母表是环绕的，所以 'a' 变成 'z' ）。
 * 请你返回对 s 进行所有移位操作以后得到的最终字符串。
 * 提示：
 * 1、1 <= s.length, shifts.length <= 5 * 10^4
 * 2、shifts[i].length == 3
 * 3、0 <= start_i <=  end_i < s.length
 * 4、0 <= direction_i <= 1
 * 5、s 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/shifting-letters-ii
 */
public class Q2381 {

    public static void main(String[] args) {
        // "ace"
        System.out.println(new Q2381().shiftingLetters("abc", stringToInt2dArray("[[0,1,0],[1,2,1],[0,2,1]]")));
        // "catz"
        System.out.println(new Q2381().shiftingLetters("dztz", stringToInt2dArray("[[0,0,0],[1,1,1]]")));
    }

    // 差分数组
    public String shiftingLetters(String s, int[][] shifts) {
        int n = s.length();
        long[] diff = new long[n + 1];
        for (int[] shift : shifts) {
            int d = shift[2] == 0 ? -1 : 1;
            diff[shift[0]] += d;
            diff[shift[1] + 1] -= d;
        }
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (i > 0) diff[i] += diff[i - 1];
            // java 精度修正
            ans.append((char) ((s.charAt(i) - 'a' + diff[i] % 26 + 26) % 26 + 'a'));
        }
        return ans.toString();
    }

}
