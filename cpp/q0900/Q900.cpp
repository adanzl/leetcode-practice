/**
 * 给定一个非负整数数组A，如果该数组每对相邻元素之和是一个完全平方数，则称这一数组为正方形数组。
 * 返回 A 的正方形排列的数目。两个排列 A1 和 A2不同的充要条件是存在某个索引i，使得 A1[i] != A2[i]。
 * 提示：
 * 1、1 <= A.length <= 12
 * 2、0 <= A[i] <= 1e9
 * 链接：https://leetcode.cn/problems/number-of-squareful-arrays/
 */

#include <bits/stdc++.h>

using namespace std;

class Solution {
  public:
    bool isInt(double f) { return floor(f) == ceil(f); }

    int numSquarefulPerms(vector<int> nums) {
        int n = nums.size();
        map<vector<int>, int> dp;
        for (int i = 0; i < n; i++)
            dp[vector({nums[i]})] = 1 << i;
        for (int _ = 1; _ < n; _++) {
            map<vector<int>, int> ndp;
            for (auto &entry : dp) {
                auto k = entry.first;
                int v = entry.second;
                for (int i = 0; i < n; i++) {
                    if (v & (1 << i))
                        continue;
                    int num = nums[i];
                    if (isInt(sqrt(num + k[0]))) {
                        vector<int> ks = {num};
                        ks.insert(ks.end(), k.begin(), k.end());
                        ndp[ks] = v | (1 << i);
                    }
                    for (int j = 1; j < k.size(); j++) {
                        if (isInt(sqrt(num + k[j - 1])) && isInt(sqrt(num + k[j]))) {
                            vector<int> ks;
                            ks.insert(ks.end(), k.begin(), k.begin() + j);
                            ks.emplace_back(num);
                            ks.insert(ks.end(), k.begin() + j, k.end());
                            ndp[ks] = v | (1 << i);
                        }
                    }
                    if (isInt(sqrt(num + k[k.size() - 1]))) {
                        vector<int> ks;
                        ks.insert(ks.end(), k.begin(), k.end());
                        ks.emplace_back(num);
                        ndp[ks] = v | (1 << i);
                    }
                }
            }
            dp = ndp;
        }
        return dp.size();
    }
};

int main(int argc, char **argv) {
    // 1
    std::cout << Solution().numSquarefulPerms(vector({2, 2, 2, 2, 2, 2, 2, 2, 2})) << endl;
    // 2
    std::cout << Solution().numSquarefulPerms(vector({1, 17, 8})) << endl;
    return 0;
}