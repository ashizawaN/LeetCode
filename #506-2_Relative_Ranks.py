from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        MIN_SCORE = 0
        MAX_SCORE = 10**6
        MIN_LENGTH = 1
        MAX_LENGTH = 10**4
        count = 0
        assert type(score) == list, "The type of score should be list."
        for i in range(len(score)-1):
            if type(score[i]) != "int":
                count += 1
        if count == 0:
            assert "The type of a value in nums sould be integer."
        if len(score) < MIN_LENGTH or len(score) > MAX_LENGTH:
            raise ValueError("The range of score should be 1 or more and 10**4 or less.")
        for i in range(len(score)-1):
            if score[i] < MIN_SCORE or score[i] > MAX_SCORE:
                raise ValueError("The value of score should be 1 or more and 10**6 or less")

        sort_score = sorted(score, reverse=True)
        ans = {}
        for i in range(len(score)):
            if i == 0:
                ans[sort_score[i]] = "Gold Medal"
            elif i == 1:
                ans[sort_score[i]] = "Silver Medal"
            elif i == 2:
                ans[sort_score[i]] = "Bronze Medal"
            else:
                ans[sort_score[i]] = str(i+1)
        return list(map(lambda x: ans[x], score))
