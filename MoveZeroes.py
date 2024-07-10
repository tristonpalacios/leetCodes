def moveZeroes(nums: list[int]) -> None:
    # Create lists for non-zero and zero elements
        b = [x for x in nums if x != 0]
        c = [y for y in nums if y == 0]

        # Modify the original list in place
        nums[:] = b + c

# moveZeroes([0,1,0,3,12])
# moveZeroes([0])
moveZeroes([0,0,1])