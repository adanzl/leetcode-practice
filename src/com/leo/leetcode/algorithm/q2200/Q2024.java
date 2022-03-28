package com.leo.leetcode.algorithm.q2200;

/**
 * 一位老师正在出一场由 n 道判断题构成的考试，每道题的答案为 true （用 'T' 表示）或者 false （用 'F' 表示）。
 * 老师想增加学生对自己做出答案的不确定性，方法是 最大化 有 连续相同 结果的题数。（也就是连续出现 true 或者连续出现 false）。
 * 给你一个字符串 answerKey ，其中 answerKey[i] 是第 i 个问题的正确结果。除此以外，还给你一个整数 k ，表示你能进行以下操作的最多次数：
 * 每次操作中，将问题的正确答案改为 'T' 或者 'F' （也就是将 answerKey[i] 改为 'T' 或者 'F' ）。
 * 请你返回在不超过 k 次操作的情况下，最大 连续 'T' 或者 'F' 的数目。
 * 提示：
 * 1、n == answerKey.length
 * 2、1 <= n <= 5 * 10^4
 * 3、answerKey[i] 要么是 'T' ，要么是 'F'
 * 4、1 <= k <= n
 * 链接：https://leetcode-cn.com/problems/maximize-the-confusion-of-an-exam
 */
public class Q2024 {
    // 双指针滑窗
    public static void main(String[] args) {
        // 5
        System.out.println(new Q2024().maxConsecutiveAnswers("TTFTTFTT", 1));
        // 3
        System.out.println(new Q2024().maxConsecutiveAnswers("TFFT", 1));
        // 4
        System.out.println(new Q2024().maxConsecutiveAnswers("TTFF", 2));
    }

    public int maxConsecutiveAnswers(String answerKey, int k) {
        int len = answerKey.length(), ret = 0, l = 0, r = 0, T = 0, F = 0;
        char[] str = answerKey.toCharArray();
        while (r < len) {
            if (str[r++] == 'T') T++;
            else F++;
            while (T > k && F > k) {
                if (str[l++] == 'T') T--;
                else F--;
            }
            ret = Math.max(ret, r - l);
        }
        return ret;
    }
}
