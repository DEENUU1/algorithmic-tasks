# Solution 1 

public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        List<int> numbers = new List<int>();

        foreach(int num in nums) {
            if (numbers.Contains(num)) {
                return true;
            }
            else {
                numbers.Add(num);
            }
        }
        return false;
    }
}

# Solution 2

public class Solution 
{
    public bool ContainsDuplicate(int[] nums) 
    {
        HashSet<int> set = new HashSet<int>(nums);
        
        return nums.Length != set.Count;
    }
}