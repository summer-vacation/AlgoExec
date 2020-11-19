#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> umap;
        for(auto &&str : strs){
            auto x = str;
            std::sort(x.begin(), x.end());

            if(umap.count(x)){
                umap[x].push_back(str);
            } else {
                umap[x] = vector<std::string>{str};
            }
        }
        vector<vector<string>> res;
        for(auto i : umap){
            res.push_back(value);
        }
        return res;
    }
};

int main(){
    Solution s;
    vector<string> strs = {"abc", "cba", "sss"};
    auto res = s.groupAnagrams(strs);

    for(auto i:res){
        for(auto x:i){
            cout << x << " ";
        }
        cout << endl;
    }
    return 0;
}
