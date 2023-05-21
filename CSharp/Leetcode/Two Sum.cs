// Solution 1

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int[] solution = new int[2];

        for (int currentIndex = 0; currentIndex < nums.Length; currentIndex++ ) {
            int searchTarget = target - nums[currentIndex];
            if (nums.Contains(searchTarget) && Array.IndexOf(nums, searchTarget) != currentIndex){
                solution[0] = currentIndex;
                solution[1] = Array.IndexOf(nums, searchTarget);
                return solution;
            }
        }
        return solution;
    }
}