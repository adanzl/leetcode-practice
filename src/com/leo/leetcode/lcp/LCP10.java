package com.leo.leetcode.lcp;

import com.leo.utils.TreeNode;

import static com.leo.utils.LCUtil.stringToTreeNode;

/**
 * 任务调度优化是计算机性能优化的关键任务之一。在任务众多时，不同的调度策略可能会得到不同的总体执行时间，因此寻求一个最优的调度方案是非常有必要的。
 * 通常任务之间是存在依赖关系的，即对于某个任务，你需要先完成他的前导任务（如果非空），才能开始执行该任务。
 * 我们保证任务的依赖关系是一棵二叉树，其中 root 为根任务，root.left 和 root.right 为他的两个前导任务（可能为空），root.val 为其自身的执行时间。
 * 在一个 CPU 核执行某个任务时，我们可以在任何时刻暂停当前任务的执行，并保留当前执行进度。
 * 在下次继续执行该任务时，会从之前停留的进度开始继续执行。暂停的时间可以不是整数。
 * 现在，系统有两个 CPU 核，即我们可以同时执行两个任务，但是同一个任务不能同时在两个核上执行。给定这颗任务树，请求出所有任务执行完毕的最小时间。
 * 限制：
 * 1、1 <= 节点数量 <= 1000
 * 2、1 <= 单节点执行时间 <= 1000
 * 链接：https://leetcode.cn/problems/er-cha-shu-ren-wu-diao-du
 */
public class LCP10 {

    public static void main(String[] args) {
        // 121
        System.out.println(new LCP10().minimalExecTime(stringToTreeNode("[47, 74, 31]")));
        // 121
        System.out.println(new LCP10().minimalExecTime1(stringToTreeNode("[47, 74, 31]")));
        // 87
        System.out.println(new LCP10().minimalExecTime(stringToTreeNode("[15, 21, null, 24, null, 27, 26]")));
        // 7.5
        System.out.println(new LCP10().minimalExecTime(stringToTreeNode("[1,3,2,null,null,4,4]")));
    }

    /**
     * 能完成前置任务的最优时间就是其单核完成所有前置任务的总时间除以2。
     * 可能会遇到这样一种情况（例如样例1），其中一项任务比另一项任务所花费的时间长的多时，并且 [只剩] 这两个任务，此时其中一个CPU就需要等另一个CPU执行完才能往下执行了。
     * 这时能完成当前节点所有前置任务的局部最优解就是其两个子树分别拥有两个CPU 并行 执行任务所花费时间的最大值。
     * 对于左右子树可以同时执行完的情况，即我们之前提到的最优解（说白了就是看其中一个子树执行完能不能多出来时间匀给另一颗子树）。
     * 全局最优解就一定是这两种情况下所花费时间的最大值。
     * 1、左右子树各用 [双] CPU 执行任务所花费时间的最大值
     * 2、左右子树各用 [单] CPU 执行任务所花费时间的最大值
     */
    public double minimalExecTime1(TreeNode root) {
        if (root == null) return 0;
        double lTime = minimalExecTime(root.left);
        double rTime = minimalExecTime(root.right);
        double case1 = Math.max(lTime, rTime);
        double case2 = (getSum(root.left) + getSum(root.right)) / 2.0;
        return Math.max(case1, case2) + root.val;
    }

    double getSum(TreeNode root) {
        if (null == root) return 0;
        return root.val + getSum(root.left) + getSum(root.right);
    }

    /**
     * 1、定义递归函数，返回两个值，分别是完成以 root 为根的子树所需要的最优并行时间 p 和串行时间 s，s + 2 * p为全部耗时。
     * 2、如果 root 为空，返回 [0,0]。
     * 3、递归左右子节点，返回 [lp,ls] 以及 [rp,rs]。不妨假设 ls ≤ rs，不满足则交换左右子树。
     * 4、如果 ls + 2 * lp ≥ rs 则可以拿出左子树的并行时间 t，让 ls + 2 * t = rs，这样会提高并行度，使得左右子树可以完美利用两个 CPU 并行执行。
     * 最终，p = rp + lp − (rs − ls) / 2 + rs 和 s = root.val。(此种情况可以优化为最优解）
     * 5、如果 ls + 2 * lp < rs，则说明无论如何完成左右子树都有一个 CPU 最终闲置，此时为了最大化并行度，让一个 CPU 跑左子树，另一个 CPU 跑右子树。
     * 最终，p = rp + ls + 2 * lp 和 s = rs − (ls + 2 * lp) + root.val。（rp不变lp * 2 + ls 都变为并行）
     */
    public double minimalExecTime(TreeNode root) {
        double[] ans = solve(root);
        return ans[0] + ans[1];
    }

    double[] solve(TreeNode root) {
        if (root == null) return new double[]{0, 0};
        double[] l = solve(root.left);
        double[] r = solve(root.right);
        if (l[1] > r[1]) {
            double[] tmp = l;
            l = r;
            r = tmp;
        }
        double lp = l[0], ls = l[1];
        double rp = r[0], rs = r[1];
        if (ls + 2 * lp >= rs) return new double[]{rp + lp - (rs - ls) / 2 + rs, root.val};
        return new double[]{rp + ls + 2 * lp, rs - (ls + 2 * lp) + root.val};
    }
}
