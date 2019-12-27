#include <iostream>
#include <queue>
#include <string>
#include <unordered_set>
#include <algorithm>
using namespace std;

// 用队列 + hash表
class Solution {
  public:
    int lengthOfLongestSubstring(string s) {
        std::queue<char> q;
        std::unordered_set<char> uset;
        size_t res = 0;
        for(auto i : s){
            if(uset.count(i)){
                while(!q.empty()){
                    auto x = q.front();
                    q.pop();
                    uset.erase(x);
                    if(x == i) {
                        q.push(i);
                        uset.insert(i);
                        res = max(res, q.size());
                        break;
                    }
                }
            } else {
                uset.insert(i);
                q.push(i);
                res = max(res, q.size());
            }
        }
        return res;
    }
};

int main(){
    Solution s;
    std::string str = "aabaabcd";
    cout << s.lengthOfLongestSubstring(str);
    return 0;
}