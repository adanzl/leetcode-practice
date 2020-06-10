package com.leo.leetcode.algorithm;

import com.leo.utils.LCUtil;
import org.junit.Test;

import java.util.Arrays;

public class Q739 {
    @Test
    public void TestOJ() {
        // [8,1,5,4,3,2,1,1,0,0]
        System.out.println(Arrays.toString(dailyTemperatures(LCUtil.stringToIntegerArray("[89,62,70,58,47,47,46,76,100,70]"))));
        // [1,1,1,4,2,1,1,0,0,0]
        System.out.println(Arrays.toString(dailyTemperatures(LCUtil.stringToIntegerArray("[30,73,74,75,71,69,72,100,76,73]"))));
    }

    public int[] dailyTemperatures(int[] T) {
        int[] flag = new int[71], out = new int[T.length];
        Arrays.fill(flag, -1);
        for (int i = T.length - 1; i >= 0; i--) {
            int v = T[i] - 30;
            flag[v] = i;
            for (int j = v + 1; j < 71; j++) {
                if (flag[j] != -1) {
                    out[i] = out[i] == 0 ? flag[j] - i: Math.min(out[i], flag[j] - i);
                }
            }

        }
        return out;
    }
}
