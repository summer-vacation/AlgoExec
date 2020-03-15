package top.interview.SortingAndSearching;

/**
 * https://leetcode.com/explore/featured/card/top-interview-questions-easy/96/sorting-and-searching/774/
 * 找到第一个isBadVersion() true的版本
 * 二分查找，，如果isBadVersion(mid)==true, 就找low-mid
 * 如果isBadVersion(mid)==false, 就找mid-high
 */
public class FirstBadVersion {

    public int firstBadVersion(int n) {
        return helper(1, n);
    }

    public int helper(int low, int high) {
        if (low >= high) return low;
        else {
            int mid = low + (high - low) / 2;
            if (isBadVersion(mid)) return helper(low, mid);
            else return helper(mid+1, high);
        }
    }

    private boolean isBadVersion(int version){
        return true;
    }
}
