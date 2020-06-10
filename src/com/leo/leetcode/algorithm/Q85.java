package com.leo.leetcode.algorithm;

import java.util.Arrays;

import org.junit.Test;

public class Q85 {
    @Test
    public void TestOJ() {
        System.out.println(maximalRectangle(new char[][] { { '1', '0', '1', '0', '0' }, { '1', '0', '1', '1', '1' },
                { '1', '1', '1', '1', '1' }, { '1', '0', '0', '1', '0' } })); // 6
    }

    /**
     * height[]: height[x] = row[x] == '1' ? (preHeight[x] + 1): 0 <br/>
     * left[]: left[x] = row[x] == '0' ? -1 : max(preLeft[x], curLeft) <br/>
     * right[]: right[x] = row[x] == '0' ? len : min(preRight[x], curRight)
     */
    public int maximalRectangle(char[][] matrix) {
        if (matrix.length == 0)
            return 0;
        int maxArea = 0, len = matrix[0].length;
        int[] height = new int[len];
        int[] left = new int[len];
        int[] right = new int[len];
        Arrays.fill(right, len);

        for (char[] row : matrix) {
            int curLeft = -1, curRight = len;
            for (int j = 0; j < row.length; j++) {
                height[j] = row[j] == '1' ? height[j] + 1 : 0;
            }
            for (int j = 0; j < row.length; j++) {
                if (row[j] == '0') {
                    curLeft = j;
                    left[j] = -1;
                } else {
                    left[j] = Math.max(left[j], curLeft + 1);
                }
            }
            for (int j = row.length - 1; j >= 0; j--) {
                if (row[j] == '0') {
                    curRight = j;
                    right[j] = len;
                } else {
                    right[j] = Math.min(right[j], curRight);
                }
            }
            for (int j = 0; j < row.length; j++) {
                maxArea = Math.max(maxArea, height[j] * (right[j] - left[j]));
            }
        }
        return maxArea;
    }

}
