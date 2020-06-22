def match(string, pattern):
    if not string or not pattern:
        return
    return match_core(string, pattern)


def match_core(str, pattern):
    # 没有pattern了却还有字符串
    if len(pattern) == 0 and len(str)!=0:
        return False

    # 没有字符串了，看pattern剩下的是不是0个或者n个“'ch'*”
    if len(str) == 0:
        while len(pattern)>=2 and pattern[1]=="*":
            pattern = pattern[2:]
        return len(pattern) == 0

    # 剩余pattern以"'ch'*"开头，直到string的第一个字符不是ch的时候再去掉pattern中的"'ch'*"
    if len(pattern)>=2 and pattern[1]=='*':
        if str[0] == pattern[0]:
            return match_core(str[1:],pattern)
        return match_core(str,pattern[2:])

    if str[0] == pattern[0] or pattern[0] == '.':
        return match_core(str[1:],pattern[1:])

    return False

if __name__ == "__main__":
    print(match("aaaefwe", "aa*"))
    print(match("aaaab", "aa*."))