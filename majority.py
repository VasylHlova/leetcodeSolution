class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_of_elements = {}
        set_nums = set(nums)
        for i  in set_nums :
            dict_of_elements[i]=0 
        for k in nums:
            dict_of_elements[k] += 1
        major = max(dict_of_elements , key=dict_of_elements.get)        
        return major