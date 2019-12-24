#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int firstUniqChar(string s) {
        vector<int> v(26,0);
        for(auto &&i : s){
            v[i-'a']++;
        }
        for(int j = 0;j < s.size(); j++){
            if(v[s[j]-'a']==1) return j;
        }
        return -1;
    }
};