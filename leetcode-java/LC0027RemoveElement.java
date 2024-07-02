import java.io.*;
import java.util.*;

public class LC0027RemoveElement {

    /**
     * - Use two pointers, one pointing at last valid number in nums (i.e., no val), one pointing
     *   to the actual value in nums we're currently scanning
     * - Skip over any nums matching val
     * - Copy into valid slot the current number
     *
     * Time:
     * - n = len(nums)
     * => O(n) to scan nums sequentially and filter out val
     *
     * Space:
     * => O(1) aux space for the two pointers/indexes
     */
    public int removeElement(int[] nums, int val) {
	int k = 0;
	int i = 0;
	while (i < nums.length) {
	    while (i < nums.length && nums[i] == val) {
		i++;
	    }
	    if (i < nums.length) {
		nums[k] = nums[i];
		k++;
		i++;
	    }
	}
	return k;
    }

    public static void main(String[] args) {
	test(new int[] { 3, 2, 2, 3 }, 3,
	     new int[] { 2, 2, -1, -1 }, 2);
	test(new int[] { 0, 1, 2, 2, 3, 0, 4, 2 }, 2,
	     new int[] { 0, 1, 3, 0, 4, -1, -1 ,-1 }, 5);
    }

    public static void test(int[] nums, int val, int[] expected, int expectedK) {
	var solution = new LC0027RemoveElement();
	var actualK = solution.removeElement(nums, val);

	if (expectedK != actualK) {
	    throw new RuntimeException("Fail, k doesn't match");
	}

	System.out.println("nums     = " + Arrays.toString(nums));
	System.out.println("expected = " + Arrays.toString(expected));

	for (int i = 0; i < expectedK; ++i) {
	    if (nums[i] != expected[i]) {
		throw new RuntimeException("Fail, value at " + i + " doesn't match");
	    }
	}
    }
}
