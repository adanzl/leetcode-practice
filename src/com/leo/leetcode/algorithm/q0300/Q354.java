package com.leo.leetcode.algorithm.q0300;

import java.util.*;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。
 * 当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
 * 请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
 * <p>
 * 说明:
 * 不允许旋转信封。
 * <p>
 * 链接：https://leetcode-cn.com/problems/russian-doll-envelopes
 */
public class Q354 {

    public static void main(String[] args) {
        // 5
        System.out.println(new Q354().maxEnvelopes(stringToInt2dArray("[[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]")));
        // 3
        System.out.println(new Q354().maxEnvelopes(stringToInt2dArray("[[10,17],[10,19],[16,2],[19,18],[5,6]]")));
        // 3
        System.out.println(new Q354().maxEnvelopes(stringToInt2dArray("[[30,50],[12,2],[3,4],[12,15]]")));
        // 2
        System.out.println(new Q354().maxEnvelopes(stringToInt2dArray("[[5,4],[6,4],[6,7],[2,4]]")));
        // 3
        System.out.println(new Q354().maxEnvelopes(stringToInt2dArray("[[5,4],[6,4],[6,7],[2,3]]")));
        // 7
        System.out.println(new Q354().maxEnvelopes(stringToInt2dArray("[[1,2],[2,3],[3,4],[4,5],[5,6],[5,5],[6,7],[7,8]]")));
        // 4
        System.out.println(new Q354().maxEnvelopes(stringToInt2dArray("[[4,5],[4,6],[6,7],[2,3],[1,1]]")));
        // 1
        System.out.println(new Q354().maxEnvelopes(stringToInt2dArray("[[1,1]]")));
        // 0
        System.out.println(new Q354().maxEnvelopes(stringToInt2dArray("[]")));
    }

    public int maxEnvelopes(int[][] envelopes) {
        int ret = 0, length = envelopes.length;
        Arrays.sort(envelopes, ((o1, o2) -> o1[0] == o2[0] ? o2[1] - o1[1] : o1[0] - o2[0]));
        int[] dp = new int[length + 1];
        dp[0] = -1;
        for (int[] envelope : envelopes) {
            int num = envelope[1];
            if (num > dp[ret]) {
                ret++;
                dp[ret] = num;
            } else {
                int left = 0;
                int right = ret;
                while (left < right) {
                    int mid = (left + right) >>> 1;
                    if (dp[mid] < num) left = mid + 1;
                    else right = mid;
                }
                dp[left] = Math.min(dp[left], num);
            }
        }
        return ret;
    }

}
