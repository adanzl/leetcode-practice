package com.leo.leetcode.algorithm.q0800;

import java.util.Arrays;

/**
 * 一行中有 N 张多米诺骨牌，我们将每张多米诺骨牌垂直竖立。
 * 在开始时，我们同时把一些多米诺骨牌向左或向右推。
 * 每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。
 * 同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。
 * 如果同时有多米诺骨牌落在一张垂直竖立的多米诺骨牌的两边，由于受力平衡， 该骨牌仍然保持不变。
 * 就这个问题而言，我们会认为正在下降的多米诺骨牌不会对其它正在下降或已经下降的多米诺骨牌施加额外的力。
 * 给定表示初始状态的字符串 "S" 。如果第 i 张多米诺骨牌被推向左边，则 S[i] = 'L'；如果第 i 张多米诺骨牌被推向右边，则 S[i] = 'R'；
 * 如果第 i 张多米诺骨牌没有被推动，则 S[i] = '.'。
 * 返回表示最终状态的字符串。
 * 提示：
 * 1、0 <= N <= 10^5
 * 2、表示多米诺骨牌状态的字符串只含有 'L'，'R'; 以及 '.';
 * 链接：https://leetcode-cn.com/problems/push-dominoes
 */
public class Q838 {

    public static void main(String[] args) {
        // "LL.RR.LLRRLL.."
        System.out.println(new Q838().pushDominoes(".L.R...LR..L.."));
        // "RR.L"
        System.out.println(new Q838().pushDominoes("RR.L"));
        // ""
        System.out.println(new Q838().pushDominoes(""));
    }

    public String pushDominoes(String dominoes) {
        char[] dominoesArr = dominoes.toCharArray();
        boolean bProcess;
        do {
            bProcess = false;
            char[] str = Arrays.copyOf(dominoesArr, dominoesArr.length);
            for (int i = 0; i < str.length; i++) {
                if (dominoesArr[i] == 'L' || dominoesArr[i] == 'R') continue;
                char l = '.', r = '.';
                if (i > 0) l = dominoesArr[i - 1];
                if (i < dominoesArr.length - 1) r = dominoesArr[i + 1];
                if (l == 'R' && r == 'L') continue;
                if (l == 'R') {
                    str[i] = 'R';
                    bProcess = true;
                }
                if (r == 'L') {
                    str[i] = 'L';
                    bProcess = true;
                }
            }
            dominoesArr = str;
        } while (bProcess);
        return new String(dominoesArr);
    }
}
