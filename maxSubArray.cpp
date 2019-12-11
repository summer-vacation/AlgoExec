class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(nums.empty()){
            return 0;
        }
        int res = 0, x = 0, t = std::numeric_limits<int>::min();
        
        for(int i = 0;i < nums.size();i++){
            if(x + nums[i] < 0){
                x = 0;
            }
            else{
                x += nums[i];
            }
            res = max(res, x);
            t = max(t, nums[i]);
        }
        if(res == 0){
            return t;
        }
        return res;
    }
};
