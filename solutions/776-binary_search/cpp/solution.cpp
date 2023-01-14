/* 
 * 776. Binary Search
 * Author: Artur Gasparyan
 * Date: 14 Jan 2023
 * Link: https://leetcode.com/problems/binary-search/submissions/877955526/
*/

class Solution {
public:
    Solution() {
        std::ios::sync_with_stdio(false);
        std::cin.tie(nullptr);
    }

    int search(vector<int>& nums, int target) {
        int lo = 0;
        int hi = nums.size()-1;
        int mi;

        while (lo <= hi) {
            mi = (lo + hi) / 2;

            if (nums[mi] < target) 
                lo = mi + 1;

            else if (nums[mi] > target) 
                hi = mi - 1;

            else 
                return mi;
        }

        return -1;
    }
};