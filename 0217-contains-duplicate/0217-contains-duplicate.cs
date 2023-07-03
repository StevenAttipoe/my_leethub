public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        HashSet<int> uniqueElements = new HashSet<int>();
        
        foreach (int num in nums)
        {
            if (uniqueElements.Contains(num))
                return true;
            
            uniqueElements.Add(num);
        }     
        return false; 
    }
}