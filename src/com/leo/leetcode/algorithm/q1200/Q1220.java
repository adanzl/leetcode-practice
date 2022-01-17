package com.leo.leetcode.algorithm.q1200;

/**
 * 给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：
 * <p>
 * 字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
 * 每个元音 'a' 后面都只能跟着 'e'
 * 每个元音 'e' 后面只能跟着 'a' 或者是 'i'
 * 每个元音 'i' 后面 不能 再跟着另一个 'i'
 * 每个元音 'o' 后面只能跟着 'i' 或者是 'u'
 * 每个元音 'u' 后面只能跟着 'a'
 * 由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。
 * <p>
 * 提示：
 * 1 <= n <= 2 * 10^4
 * <p>
 * 链接：https://leetcode-cn.com/problems/count-vowels-permutation
 */
public class Q1220 {

    public static void main(String[] args) {
        // 237753473
        System.out.println(new Q1220().countVowelPermutation(158));
        // 10
        System.out.println(new Q1220().countVowelPermutation(2));
        // 5
        System.out.println(new Q1220().countVowelPermutation(1));
        // 68
        System.out.println(new Q1220().countVowelPermutation(5));
        // 759959057
        System.out.println(new Q1220().countVowelPermutation(20000));
        // 1151090
        System.out.println(new Q1220().countVowelPermutation(20));
    }


    public int countVowelPermutation(int n) {
        int ret = 0, MOD = 1000000007;
        int[][] nextMap = new int[][]{
                {1},
                {0, 2},
                {0, 1, 3, 4},
                {2, 4},
                {0},
        };
        int[] size = new int[]{1, 2, 4, 2, 1};
        int[] flag = new int[]{1, 1, 1, 1, 1};
        for (int i = 0; i < n - 1; i++) {
            int[] tmp = new int[5];
            for (int j = 0; j < 5; j++) {
                int[] nextList = nextMap[j];
                for (int k = 0; k < size[j]; k++) {
                    int next = nextList[k];
                    tmp[next] = (tmp[next] + flag[j]) % MOD;
                }
            }
            flag = tmp;
        }
        for (int i = 0; i < 5; i++) ret = (ret + flag[i]) % MOD;
        return ret % MOD;
    }
}
