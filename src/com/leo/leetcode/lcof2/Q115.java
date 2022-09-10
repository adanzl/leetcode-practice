package com.leo.leetcode.lcof2;

import static com.leo.utils.LCUtil.stringToInt2dArray;
import static com.leo.utils.LCUtil.stringToIntegerArray;

/**
 * 给定一个长度为 n 的整数数组 nums ，其中 nums 是范围为 [1，n] 的整数的排列。还提供了一个 2D 整数数组 sequences ，其中 sequences[i] 是 nums 的子序列。
 * 检查 nums 是否是唯一的最短 超序列 。最短 超序列 是 长度最短 的序列，并且所有序列 sequences[i] 都是它的子序列。对于给定的数组 sequences ，可能存在多个有效的 超序列 。
 * 1、例如，对于 sequences = [[1,2],[1,3]] ，有两个最短的 超序列 ，[1,2,3] 和 [1,3,2] 。
 * 2、而对于 sequences = [[1,2],[1,3],[1,2,3]] ，唯一可能的最短 超序列 是 [1,2,3] 。[1,2,3,4] 是可能的超序列，但不是最短的。
 * 如果 nums 是序列的唯一最短 超序列 ，则返回 true ，否则返回 false 。
 * 子序列 是一个可以通过从另一个序列中删除一些元素或不删除任何元素，而不改变其余元素的顺序的序列。
 * 提示：
 * 1、n == nums.length
 * 2、1 <= n <= 10^4
 * 3、nums 是 [1, n] 范围内所有整数的排列
 * 4、1 <= sequences.length <= 10^4
 * 5、1 <= sequences[i].length <= 10^4
 * 6、1 <= sum(sequences[i].length) <= 10^5
 * 7、1 <= sequences[i][j] <= n
 * 8、sequences 的所有数组都是 唯一 的
 * 9、sequences[i] 是 nums 的一个子序列
 * 链接：https://leetcode.cn/problems/ur2n8P
 */
public class Q115 {

    public static void main(String[] args) {
        // true
        System.out.println(new Q115().sequenceReconstruction(stringToIntegerArray("[4,1,5,2,6,3]"), stringToInt2dArray("[[5,2,6,3],[4,1,5,2]]")));
        // true
        System.out.println(new Q115().sequenceReconstruction(stringToIntegerArray("[1,2,3]"), stringToInt2dArray("[[1,2],[1,3],[2,3]]")));
        // true
        System.out.println(new Q115().sequenceReconstruction(stringToIntegerArray("[1,2]"), stringToInt2dArray("[[1,2]]")));
        // false
        System.out.println(new Q115().sequenceReconstruction(stringToIntegerArray("[1,2,3]"), stringToInt2dArray("[[1,2],[1,3]]")));
        // false
        System.out.println(new Q115().sequenceReconstruction(stringToIntegerArray("[1,2,3]"), stringToInt2dArray("[[1,2]]")));
    }

    int[] parent;

    public boolean sequenceReconstruction(int[] nums, int[][] sequences) {
        int n = nums.length, count = 0;
        parent = new int[n];
        int[] idx = new int[n + 1];
        for (int i = 0; i < n; i++) {
            idx[nums[i]] = i;
            parent[i] = i;
        }
        for (int[] seq : sequences) {
            for (int i = 0; i < seq.length - 1; i++) {
                int i0 = idx[seq[i]], i1 = idx[seq[i + 1]];
                if (i1 - i0 == 1 && merge(i0, i1)) count++;
            }
        }
        return count >= n-1;
    }

    int find(int x) {
        return parent[x] == x ? parent[x] : (parent[x] = find(parent[x]));
    }

    boolean merge(int v1, int v2) {
        int r1 = find(v1), r2 = find(v2);
        if (r1 == r2) return false;
        parent[r2] = r1;
        return true;
    }
}
