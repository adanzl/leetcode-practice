package com.leo.leetcode.algorithm.q2200;

/**
 * 在一条无限长的公路上有 n 辆汽车正在行驶。汽车按从左到右的顺序按从 0 到 n - 1 编号，每辆车都在一个 独特的 位置。
 * 给你一个下标从 0 开始的字符串 directions ，长度为 n 。directions[i] 可以是 'L'、'R' 或 'S' 分别表示第 i 辆车是向 左 、向 右 或者 停留 在当前位置。每辆车移动时 速度相同 。
 * 碰撞次数可以按下述方式计算：
 * 当两辆移动方向 相反 的车相撞时，碰撞次数加 2 。
 * 当一辆移动的车和一辆静止的车相撞时，碰撞次数加 1 。
 * 碰撞发生后，涉及的车辆将无法继续移动并停留在碰撞位置。除此之外，汽车不能改变它们的状态或移动方向。
 * 返回在这条道路上发生的 碰撞总次数 。
 * 提示：
 * 1、1 <= directions.length <= 10^5
 * 2、directions[i] 的值为 'L'、'R' 或 'S'
 * 链接：https://leetcode-cn.com/problems/count-collisions-on-a-road
 */
public class Q2211 {

    public static void main(String[] args) {
        // 20
        System.out.println(new Q2211().countCollisions("SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"));
        // 5
        System.out.println(new Q2211().countCollisions("RLRSLL"));
        // 0
        System.out.println(new Q2211().countCollisions("LLRR"));
    }

    public int countCollisions(String directions) {
        int ret = 0, count = 1;
        char s = directions.charAt(0);
        for (int i = 1; i < directions.length(); i++) {
            char d = directions.charAt(i);
            if (d == 'R') {
                if (s == 'R') count++;
                s = d;
            } else if (d == 'S') {
                if (s == 'R') ret += count;
                s = d;
                count = 1;
            } else { // d == L
                if (s == 'R') {
                    ret += count + 1;
                    s = 'S';
                } else if (s == 'L') {
                    s = d;
                } else { // s == S
                    ret++;
                    s = 'S';
                }
                count = 1;
            }
        }
        return ret;
    }
}
