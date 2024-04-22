'''Restituisci gli elementi in comune tra le due liste'''

def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    for i in nums1:
        return nums2.count(i)
    
print(intersection([3, 1, 4], [2, 3, 0]))