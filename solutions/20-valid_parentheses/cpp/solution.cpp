/*
 * Problem 2. Valid Parenthesis
 * Author: Artur Gasparyan
 * Date: 30 Dec 2022
 * Link: https://leetcode.com/problems/valid-parentheses/submissions/868249682/
*/

class Solution {
public:
    bool isValid(string s) {
        std::stack<char> closerStack;

        for (int i = 0; i < s.length(); ++i) {
            char c = s[i];

            if (isOpener(c)) {
                closerStack.push(c);

            }
            else {
                if (closerStack.empty() || closerStack.top() != getOpener(c))
                    return false;
                    
                closerStack.pop();
            }
        }

        return closerStack.empty();
    }


private:
    const bool isOpener(const char c) {
        return c == '(' || c == '[' || c == '{'; 
    }

    const char getOpener(const char c) {
        switch (c) {
            case ')':
                return '(';
            case ']':
                return '[';
            case '}':
                return '{';
            default:
                return 'X';
        }
    }
};