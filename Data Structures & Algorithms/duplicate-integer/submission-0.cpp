#include <unordered_map>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, bool> seenNums;
        for (int n : nums) {
            if (seenNums[n]) {
                return true;
            }
            seenNums[n] = true;
        }
        return false;
    }
};