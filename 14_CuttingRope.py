class Solution:

    def cuttingRope1(self, n):
        """
        dp,f(n) = max(f(i)*f(n-i))
        由于必须剪一刀，所以对n<=3单独考虑
        """
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        porduct = [0] * (n + 1)
        porduct[0] = 0
        porduct[1] = 1
        porduct[2] = 2
        porduct[3] = 3

        res = 0
        for i in range(4, n + 1):
            maxs = 0
            for j in range(1, i // 2 + 1):
                pro = porduct[j] * porduct[i - j]
                maxs = max(maxs, pro)

            porduct[i] = maxs

        res = porduct[-1]
        return res

    def cuttingRope2(self, n):
        """
        贪婪法，当
        """
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        time_of_3 = n // 3
        if n - time_of_3 == 1:
            time_of_3 -= 1

        time_of_2 = (n - time_of_3*3)//2
        return pow(3,time_of_3)*pow(2,time_of_2)

if __name__ == '__main__':
    s = Solution()
    res1 = s.cuttingRope1(6)
    res2 = s.cuttingRope2(6)
    print(res1)
    print(res2)
