class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if arr[i] % 2 == 1 and i <= arr.index(arr[-3]):
                if arr[i + 1] % 2 == 1:
                    if arr[i + 2] % 2 == 1:
                        return True
        
        return False