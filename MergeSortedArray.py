def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    end_index = len(nums1) - 1
    while m > 0 and n > 0:
        if nums2[n - 1] >= nums1[m - 1]:
            nums1[end_index] = nums2[n - 1]
            n -= 1
        else:
            nums1[end_index] = nums1[m - 1]
            m -= 1
        end_index -= 1

    while n > 0:  # edge case when nums1 is empty
        nums1[end_index] = nums2[n - 1]
        n -= 1
        end_index -= 1
    print(nums1)





merge([1,2,3,0,0,0],3,[2,5,6],3)