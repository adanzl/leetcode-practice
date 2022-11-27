/**
 * 链接：https://leetcode.cn/problems/count-subarrays-with-median-k/
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {

  private:
    int t[200005];

  public:
    int countSubarrays(const vector<int> &nums, int k) {
        int n = nums.size(), i, j;
        vector<int> s(n + 1);
        for (i = 0; i < n; i++) {
            if (nums[i] > k)
                s[i + 1] = s[i] + 1;
            else if (nums[i] < k)
                s[i + 1] = s[i] - 1;
            else {
                j = i;
                s[i + 1] = s[i];
            }
        }
        for (i = 0; i <= j; i++)
            t[s[i] + n]++;
        int ans = 0;
        for (; i <= n; i++)
            ans += t[s[i] + n] + t[s[i] + n - 1];
        return ans;
    }
};

int main() {
    // 3
    cout << (new Solution())->countSubarrays(vector<int>({3, 2, 1, 4, 5}), 4) << endl;
    // 1
    cout << (new Solution())->countSubarrays(vector<int>({2, 3, 1}), 3) << endl;
    // 1
    cout << (new Solution())->countSubarrays(vector<int>({10, 3, 8, 5, 6, 7, 2, 9, 4, 1}), 9) << endl;
    return 0;
}