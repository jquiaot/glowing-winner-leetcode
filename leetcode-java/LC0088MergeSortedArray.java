import java.io.*;
import java.util.*;

public class LC0088MergeSortedArray {

    /**
     * - Two pointers keeping track of positions in nums1 and nums2.
     * - Start from end of nums1 and nums2, and fill nums1 from back.
     * - When we've exhausted either nums1 or nums2, fill in rest of values
     *   into nums1 as needed.
     *
     * Time:
     * => O(m + n) - traversal of nums1 elements and nums2 elements once
     *               since they're already sorted
     *
     * Space:
     * => O(1) aux space for storing pointers/indexes into nums1 and nums2
     */
    public void merge(int[] nums1, int m, int[] nums2, int n) {
	if (n == 0) {
	    return;
	} else if (m == 0) {
	    for (int i = 0; i < n; ++i) {
		nums1[i] = nums2[i];
	    }
	    return;
	}

	int i = m - 1; // index into nums1 elements
	int j = n - 1; // index into nums2 elements
	int k = m + n - 1; // index into actual nums1 array (including buffer)

	while (i >= 0 && j >= 0) {
	    if (nums1[i] > nums2[j]) {
		nums1[k] = nums1[i];
		i--;
	    } else {
		nums1[k] = nums2[j];
		j--;
	    }
	    k--;
	}
	/*
	System.out.println(String.format("nums1=" + Arrays.toString(nums1) + "," +
					 "nums2=" + Arrays.toString(nums2) + "," +
					 "i=" + i + ", j=" + j + ", k=" + k));
	*/

	// nums1 exhausted but nums2 isn't, so just copy over nums2 values
	// into remaining slots of nums1
	if (j >= 0) {
	    while (j >= 0) {
		nums1[k] = nums2[j];
		k--;
		j--;
	    }
	}
	// note if nums2 is exhausted, the remaining elements in nums1 are
	// already sorted and so we don't have to do anything (already in
	// destination array nums1)
    }

    public static void main(String[] args) {
	test(new int[] { 1, 2, 3, 0, 0, 0 }, 3,
	     new int[] { 2, 5, 6 }, 3,
	     new int[] { 1, 2, 2, 3, 5, 6 });
	test(new int[] { 1 }, 1,
	     new int[0], 0,
	     new int[] { 1, });
	test(new int[] { 0 }, 0,
	     new int[] { 1 }, 1,
	     new int[] { 1 });
	test(new int[] { 2, 0 }, 1,
	     new int[] { 1 }, 1,
	     new int[] { 1, 2 });
    }

    private static void test(int[] nums1, int m, int[] nums2, int n,
			     int[] expected) {
	var solution = new LC0088MergeSortedArray();
	solution.merge(nums1, m, nums2, n);
	if (!Arrays.equals(expected, nums1)) {
	    throw new RuntimeException("Fail");
	}
	// System.out.println(Arrays.toString(nums1));
    }
}
