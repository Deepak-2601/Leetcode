nums = [2, 2, 1]
q = len(nums)
if q != 1:
    for i in range(q - 1, -1, -1):
        x = nums[i]
        for j in range(i + 1, q):
            if x == nums[j]:
                nums.remove(nums[j])
                nums.remove(x)
                q -= 2
                break
    print(nums[0])
