
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        """
        to save space, we only need to memorize the n - 1 and n - 2 number

        :param n:
        :return:
        """

        fib = [0, 1]
        for i in range(2, n + 1, 1):
            fib[i % 2] = fib[0] + fib[1]
        return fib[(n + 1) % 2]

    def naive_fib(self, n):
        """
        to save some time, we can memorize the result
        space: O(n)
        :param n:
        :return:
        """
        series = [0, 1]
        for i in range(2, n + 1):
            series[i].append(series[i - 2] + series[i - 1])
        return series[-1]


    def recur_fib(self, n):
        """
        recursion, first solution to come up with
        time: O(2^n)
        :param n:
        :return:
        """

        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.recur_fib(n - 1) + self.recur_fib(n - 2)
