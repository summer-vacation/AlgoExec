#include <iostream>
#include <set>
#include <unordered_set>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    template <class T>
    static void hash_combine(std::size_t &seed, T v) {
        seed ^= std::hash<T>()(v) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
    }

    struct HashFunc {
        template <class T>
        std::size_t operator()(const std::vector<T> &v) const {
            size_t seed = 0;
            for(T i:v){
                hash_combine(seed, i);
            }
            return seed;
        }
    };
    
    vector<vector<int>> threeSum(vector<int>& nums) {
        if(nums.size() < 3) return vector<vector<int>>(); 
        sort(nums.begin(), nums.end());
        unordered_set<vector<int>, HashFunc> res_set;
        
        for(int i = 0;i<nums.size()-2;i++){
            for(int j = i+1; j<nums.size()-1;j++){
                int target = 0-nums[i]-nums[j];
                
                if(binary_search(nums.begin()+j+1, nums.end(),target)){
                    res_set.insert(vector<int>({nums[i], nums[j],target}));
                }

                while((j < nums.size() - 1) && (nums[j] == nums[j+1])){
                    j++;
                }
            }
        }
        vector<vector<int>> res;
        for(auto i:res_set){
            res.push_back(i);
        }
        return res;
    }
};

int main(){
    Solution x;
    vector<int> nums = {-1, 0, 2, 1, -1};
    auto r = x.threeSum(nums);
    for(auto i:r){
        for(auto p: i){
            cout << p << " ";
        }
        cout << endl;
    }
}