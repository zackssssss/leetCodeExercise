from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort()

        curr = intervals[0]
        res = []

        for interval in intervals:
            if interval[0] <= curr[1]:
                curr[1] = max(interval[1], curr[1])
            else:
                res.append(curr)
                curr = interval
        res.append(curr)
        return res


if __name__ == '__main__':
    intervals = [[1, 10], [8, 9], [2, 6], [15, 18]]
    s = Solution()
    print(s.merge(intervals))
