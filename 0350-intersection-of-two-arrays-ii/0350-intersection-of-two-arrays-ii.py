class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3 = []

        for num in nums1:
            if num in nums2:
                nums3.append(num)

        return nums3