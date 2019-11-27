func firstUniqChar(s string) int {
    v := make([]int, 26)
    
    for _, i := range s {
        v[i-'a']++
    }
    
    for j, _ := range s {
        if v[s[j]-'a']==1 {
            return j
        }
    }
    
    return -1;
}