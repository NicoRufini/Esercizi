'''Data una lista di interi spostare gli zeri alla fine mantenendo l'ordine dei numeri che non sono zero'''

def move_zeroes(nums: list[int]) -> list:
    for i in nums:
        nums.remove(0)
        nums.append(0)
    return nums

print(move_zeroes([1, 0, 1, 1, 0, 1]))