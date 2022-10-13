from collections import defaultdict

def delete_earn(nums):
    num_dict = defaultdict(int)
    # {

    # }
    max_num = nums[0]

    for num in nums:
        num_dict[num] += num
        max_num = max(max_num, num)

    # {
        # 0 : 0,
        # 1 : 34,
        # 2 : 27
    # }
    # Base cases
    points = [0] * (max_num + 1)
    points[1] = num_dict[1]

    for i in range(2, len(points)):
        points[i] = max(points[i-1], points[i-2] + num_dict[i])

    return points[-1]

print(delete_earn([3,4,2]))
print(delete_earn([2,2,3,3,3,4]))
    
