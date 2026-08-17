class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> s = new HashSet<>();
        
        for(int i: nums){
            if(!s.add(i)){
                return true;
            }   