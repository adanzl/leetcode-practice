package com.leo.leetcode.algorithm.q5000;

import static com.leo.utils.LCUtil.stringToInt2dArray;

/**
 * 存在一个 n x n 大小、下标从 0 开始的网格，网格中埋着一些工件。
 * 给你一个整数 n 和一个下标从 0 开始的二维整数数组 artifacts ，artifacts 描述了矩形工件的位置，其中 artifacts[i] = [r1i, c1i, r2i, c2i] 表示第 i 个工件在子网格中的填埋情况：
 * (r1i, c1i) 是第 i 个工件 左上 单元格的坐标，且
 * (r2i, c2i) 是第 i 个工件 右下 单元格的坐标。
 * 你将会挖掘网格中的一些单元格，并清除其中的填埋物。如果单元格中埋着工件的一部分，那么该工件这一部分将会裸露出来。如果一个工件的所有部分都都裸露出来，你就可以提取该工件。
 * 给你一个下标从 0 开始的二维整数数组 dig ，其中 dig[i] = [ri, ci] 表示你将会挖掘单元格 (ri, ci) ，返回你可以提取的工件数目。
 * 生成的测试用例满足：
 * 1、不存在重叠的两个工件。
 * 2、每个工件最多只覆盖 4 个单元格。
 * 3、dig 中的元素互不相同。
 * 提示：
 * 1、1 <= n <= 1000
 * 2、1 <= artifacts.length, dig.length <= min(n^2, 10^5)
 * 3、artifacts[i].length == 4
 * 4、dig[i].length == 2
 * 5、0 <= r1i, c1i, r2i, c2i, ri, ci <= n - 1
 * 6、r1i <= r2i
 * 7、c1i <= c2i
 * 8、不存在重叠的两个工件
 * 9、每个工件 最多 只覆盖 4 个单元格
 * 10、dig 中的元素互不相同
 * 链接：https://leetcode-cn.com/problems/count-artifacts-that-can-be-extracted
 */
public class Q5203 {

    public static void main(String[] args) {
        // 0
        System.out.println(new Q5203().digArtifacts(6, stringToInt2dArray("[[0,2,0,5],[0,1,1,1],[3,0,3,3],[4,4,4,4],[2,1,2,4]]"), stringToInt2dArray("[[0,2],[0,3],[0,4],[2,0],[2,1],[2,2],[2,5],[3,0],[3,1],[3,3],[3,4],[4,0],[4,3],[4,5],[5,0],[5,1],[5,2],[5,4],[5,5]]")));
        // 1
        System.out.println(new Q5203().digArtifacts(2, stringToInt2dArray("[[0,0,0,0],[0,1,1,1]]"), stringToInt2dArray("[[0,0],[0,1]]")));
        // 2
        System.out.println(new Q5203().digArtifacts(2, stringToInt2dArray("[[0,0,0,0],[0,1,1,1]]"), stringToInt2dArray("[[0,0],[0,1],[1,1]]")));
    }

    public int digArtifacts(int n, int[][] artifacts, int[][] dig) {
        int[] count = new int[artifacts.length];
        int[][] map = new int[n][n];
        int ret = 0;
        for (int i = 0; i < artifacts.length; i++) {
            int[] artifact = artifacts[i];
            count[i] = (artifact[2] - artifact[0] + 1) * (artifact[3] - artifact[1] + 1);
            for (int j = artifact[0]; j <= artifact[2]; j++) {
                for (int k = artifact[1]; k <= artifact[3]; k++) {
                    map[j][k] = i + 1;
                }
            }
        }
        for (int[] d : dig) {
            int i = map[d[0]][d[1]];
            if (i > 0 && --count[i - 1] == 0) ret++;
        }
        return ret;
    }
}
