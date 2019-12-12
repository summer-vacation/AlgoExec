class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int sz = prices.size();
        if(sz <= 1) return 0;

        int res = 0;
        int m = prices[0];
        for(int i = 1;i < prices.size();i++){
            res = max(res, prices[i] - m);
            m = min(m, prices[i]);
        }
        return res;
    }
};

class Solution2 {
public:
    int maxProfit(vector<int>& prices) {
        int sz = prices.size();
        if(sz <= 1) return 0;

        vector<int> left(sz, 0);
        vector<int> right(sz, 0);
        left[0] = prices[0];
        right[sz-1] = prices[sz-1];
        for(int i = 1; i < sz; i++){
            if(prices[i] < left[i-1]){
                left[i] = prices[i];
            } else {
                left[i] = left[i-1];
            }
        }
        for(int i = sz-2;i >= 0;i--){
            if(prices[i] > right[i+1]){
                right[i] = prices[i];
            } else {
                right[i] = right[i+1];
            }
        }
        int res = 0;
        for(int i = 0; i < sz - 1; i++){
            res = max(res, right[i+1] - left[i]);
        }
        return res;
    }
};
