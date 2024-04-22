'''data una lista di numeri, restituire l'elemento che compare più di 2 volte'''

def majority_element(nums: list[int]) -> int:
    for i in nums:
        if nums.count(i) > len(nums) / 2:
            print(i)
            return i
    return None
