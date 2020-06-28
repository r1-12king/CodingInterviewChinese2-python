def longest_substring_without_duplication(s):
    pos = [-1] * 26
    dp = [0] * len(s)
    dp[0] = 1
    pos[ord(s[0]) - ord('a')] = 0

    for i in range(1, len(s)):
        preindex = pos[ord(s[i]) - ord('a')]
        if preindex < 0 or i - preindex > dp[i - 1]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = i - preindex

        pos[ord(s[i]) - ord('a')] = i

    return max(dp)


if __name__ == "__main__":
    print(longest_substring_without_duplication("abcdefghijklmn"))
