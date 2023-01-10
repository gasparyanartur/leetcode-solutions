/* 
 * Problem 1. Two Sum
 * Author: Artur Gasparyan
 * Date: Dec 30 2022
 * Link: https://leetcode.com/problems/two-sum/submissions/868242788/
*/ 

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {        
       
        std::unordered_map<int, int> diffToIndex{};

        for (int i = 0; i < nums.size(); ++i) {
            int num = nums[i];
            int diff = target - num;

            if (diffToIndex.find(num) != diffToIndex.end())
                return std::vector<int>{diffToIndex[num], i};
            
            diffToIndex[diff] = i;
                
        }

       return std::vector<int>{};
    }


};