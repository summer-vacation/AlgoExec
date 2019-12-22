package top.interview.Design;

import java.util.*;
import java.util.stream.Collectors;

/**
 * https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/670/
 */
public class ShuffleAnArray {
    public int[] array;
    public ShuffleAnArray(int[] nums) {
        array = nums;
    }

    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        return array;
    }

    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        List<Integer> llist = Arrays.stream(array).boxed().collect(Collectors.toList());
        Collections.shuffle(llist);
        return llist.stream().mapToInt(Integer::valueOf).toArray();
    }

    public static void main(String[] args) {
        int[] nums = {1,2,3};
        ShuffleAnArray shuffleAnArray = new ShuffleAnArray(nums);
        int[] res1 = shuffleAnArray.reset();
        int[] res2 = shuffleAnArray.shuffle();
    }
}
