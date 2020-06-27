def find_greatest_sum(nums):
    if not nums:
        return 0

    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1]+nums[i],nums[i])

    return max(dp)

if __name__ == "__main__":
    print(find_greatest_sum([1, -2, 3, 10, -4, 7, 2, -5]))