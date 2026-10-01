class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numsMap;

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (numsMap.count(diff) && numsMap[diff] != i) {
                return {numsMap[diff], i};
            }
            numsMap[nums[i]] = i;
        }

        return {};
    }
};
