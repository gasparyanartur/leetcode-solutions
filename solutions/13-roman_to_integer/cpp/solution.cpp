/*
 * 13. Roman to Integer
 * Author: Artur Gasparyan
 * Date: 16 Jan 2023
 * Link: https://leetcode.com/problems/roman-to-integer/submissions/879244581/
*/


const int values[7] = {1, 5, 10, 50, 100, 500, 1000};


class Solution {
    
public:
    Solution() {
        std::ios::sync_with_stdio(false);
        std::cin.tie(nullptr);
    }

    int romanToInt(string s) {
        int index = parseIndex(s[0]);
        int sum = values[index];    
        int prevIndex = index;

        for (int i = 1; i < s.length(); ) {
            index = parseIndex(s[i++]);
            sum += values[index] - (index > prevIndex) * (2 * values[prevIndex]);
            prevIndex = index;
        }
        
        return sum;
    }
    
private:
    inline int parseIndex(char c) {
        switch(c) {
            case 'I':
                return 0;
            case 'V':
                return 1;
            case 'X':
                return 2;
            case 'L':
                return 3;
            case 'C':
                return 4;
            case 'D':
                return 5;
            case 'M':
                return 6;
            default:
                return -1;
        }
    }
};