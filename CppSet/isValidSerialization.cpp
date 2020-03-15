class Solution {
public:
    bool isValidSerialization(string preorder) {
        stack<char> s;
        bool is_null = false;
        preorder.push_back(',');
        for(int i = 0; i < preorder.size();i++) {
            if(preorder[i] == '#') is_null = true;
            else if(preorder[i] != ',') is_null = false;
            else if(preorder[i] == ',') {
                if(is_null)
                    s.push('#');
                else
                    s.push('0');
            }
        }
        for (std::stack<char> dump = s; !dump.empty(); dump.pop())
            std::cout << dump.top() << '\n';
        int cnt = 0;

        if(s.size() == 1 && s.top() == '#') {
            return true;
        }
        while(!s.empty()) {
            if(s.top() == '#') {
                s.pop();
                cnt++;
            } else {
                cnt -= 2;
                if(cnt < 0) return false;
                s.pop();
                if(s.empty()) return (cnt == 0);
                s.push('#');
            }
        }
        return (cnt == 0);
    }
};
