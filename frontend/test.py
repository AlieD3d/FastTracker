def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = set(len(nums))
        hashTable = {}
        for i in range(k):
            if nums[i] in hashTable:
                nums.pop(i)
                nums.append('_')
            hashTable[i] = nums[i]
        return k, nums

nums = [1,1,2]
expectedNums = [1,2,'_']
k = removeDuplicates(nums)
assert k[0] == len(expectedNums)
for i in k[1]:
    assert nums[i] == expectedNums[i]
