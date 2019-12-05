#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        if(amount == 0)return 1;
        
        vector<int> dp(amount + 1, 0);
        dp[0] = 1;
        for(int i = 0; i < coins.size(); i++){
            for(int j = coins[i]; j < amount + 1; j++){
                dp[j] += dp[j-coins[i]];
            }
        }
        for(int i = 0 ;i < dp.size();i++){
          cout << dp[i] << "  ";
        }
        return dp[amount];
    }
};

int main(){
  Solution x;
  vector<int> v = {1,2,5};
  cout << x.change(5, v);
  return 0;
}