def threeSum(nums):
    result = []

    nums.sort()

    for i in range(len(nums) - 2):

        start = i + 1
        end = len(nums) - 1

        if i == 0 or nums[i] != nums[i - 1]:
            while start < end:
                if nums[i] + nums[start] + nums[end] == 0:

                    result.append([nums[i], nums[start], nums[end]])

                    start += 1
                    end -= 1

                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1

                elif nums[i] + nums[start] + nums[end] < 0:
                    start += 1
                else:
                    end -= 1

    return result


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))
