class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> seen;
        for (char c : s) {
            if (seen[c]) seen[c] += 1;
            else seen[c] = 1;
        }
        for (char c : t) {
            if (seen[c]) seen[c] -= 1;
            else return false;
        }
        for (auto& [a,val] : seen) {
            if (val != 0) return false;
        }
        return true;
    }
};
