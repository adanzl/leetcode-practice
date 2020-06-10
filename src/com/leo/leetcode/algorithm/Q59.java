package com.leo.leetcode.algorithm;

public class Q59 {
    public int[][] generateMatrix(int n) {
        int[][] out = new int[n][];
        for (int i = 0; i < n; i++) {
            out[i] = new int[n];
        }
        int d = 0; // r=0, d=1, l=2, u=3
        int maxX = n - 1;
        int maxY = n - 1;
        int minX = 0, minY = 0;
        int x = 0, y = 0;
        int v = 1;
        while (maxX >= minX || maxY >= minY) {
            if (x >= minX && x <= maxX && y >= minY && y <= maxY)
                out[y][x] = v++;
            switch (d) {
                case 0:
                    x++;
                    if (x > maxX) {
                        x = maxX;
                        d = 1;
                        minY++;
                    }
                    break;
                case 1:
                    y++;
                    if (y > maxY) {
                        y = maxY;
                        d = 2;
                        maxX--;
                    }
                    break;
                case 2:
                    x--;
                    if (x < minX) {
                        x = minX;
                        d = 3;
                        maxY--;
                    }
                    break;
                case 3:
                    y--;
                    if (y < minY) {
                        y = minY;
                        d = 0;
                        minX++;
                    }
                    break;
            }
        }

        return out;
    }
}
