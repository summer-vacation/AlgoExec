class Solution {
public:
    bool makesquare(vector<int>& nums) {
        int sum = 0;
        for(auto i:nums){
            sum+=i;
        }
        if(sum%4!=0 || sum == 0)return false;
        
        int target = sum/4;
        
        sort(nums.begin(), nums.end(),[](int i, int j){return i>j;});
        
        std::vector<int> res(4, 0);
        
        if(func(target, 0, nums, res)){
            for(int r : res){
                if(r != target)return false;
            }
            return true;
        }

        return false;
    }
    
    bool func(int target, int index, const std::vector<int> &nums, std::vector<int> &res){
        if(index == nums.size())return true;
        
        for(int i = 0; i < 4;i++){
            if(res[i] + nums[index] <= target){
                res[i] += nums[index];
                if(func(target, index+1, nums, res)) return true;
                res[i] -= nums[index];
            }
        }
        return false;
    }
};
