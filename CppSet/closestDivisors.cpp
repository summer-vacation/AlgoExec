class Solution {
public:
    vector<int> closestDivisors(int num) {
        uint64_t d = num + 2;
        d = sqrt(d);
        for(uint64_t i = d; i >= 0; i--) {
            if((num + 1) % i == 0) {
                return {i, (num + 1)/i};
            }
            if((num+2) % i == 0) {
                return {i, (num+2) / i};
            }
        }
        return {0, 0};
    }
};
