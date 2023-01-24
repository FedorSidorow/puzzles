# id 79891635
def broken_search(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def test():
    # arr = [4,5,6,7,8,9,10,11,15,16,20,23,26,27,29,30,35,36,39,40,41,45,57,59,69,72,75,77,80,84,87,90,91,98,100,101,0,1,2,3]
    arr = [0, 2, 6, 7, 8, 9, 10]
    assert broken_search(arr, 5) == -1


#test()
