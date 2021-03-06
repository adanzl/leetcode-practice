package com.leo.leetcode.algorithm.q0700;

import com.leo.utils.LCUtil;

import java.util.Arrays;

public class Q739 {

    public static void main(String[] args) {
        new Q739().TestOJ();
    }

    public void TestOJ() {
        // [8,1,5,4,3,2,1,1,0,0]
        System.out.println(Arrays.toString(dailyTemperatures(LCUtil.stringToIntegerArray("[89,62,70,58,47,47,46,76,100,70]"))));
        // [1,1,1,4,2,1,1,0,0,0]
        System.out.println(Arrays.toString(dailyTemperatures1(LCUtil.stringToIntegerArray("[30,73,74,75,71,69,72,100,76,73]"))));
    }

    // Solve 1: stack
    public int[] dailyTemperatures(int[] T) {
        int[] s = new int[T.length];
        int[] out = new int[T.length];
        int iStack = 0;
        for (int i = 0; i < T.length; i++) {
            while (iStack != 0 && T[s[iStack - 1]] < T[i]) {
                int idx = s[iStack-- - 1];
                out[idx] = i - idx;
            }
            s[iStack++] = i;
        }

        return out;
    }

    // Solve 2: last index map
    public int[] dailyTemperatures1(int[] T) {
        int[] flag = new int[71], out = new int[T.length];
        Arrays.fill(flag, -1);
        for (int i = T.length - 1; i >= 0; i--) {
            int v = T[i] - 30;
            flag[v] = i;
            for (int j = v + 1; j < 71; j++) {
                if (flag[j] != -1) {
                    out[i] = out[i] == 0 ? flag[j] - i : Math.min(out[i], flag[j] - i);
                }
            }

        }
        return out;
    }
}
