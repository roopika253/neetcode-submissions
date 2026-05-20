class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(self.nums)
        self.prefix_sum = [0]*n
        self.prefix_sum[0] = nums[0]
        for i in range(1,n):
            self.prefix_sum[i] = self.prefix_sum[i-1] + nums[i]
       

        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right]-self.prefix_sum[left]+self.nums[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)