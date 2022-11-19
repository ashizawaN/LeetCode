# time complexity: O(n**2)
# space complexity: O(1)
from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats_num = [0] * (max(seats)+1)
        students_num = [0] * (max(students)+1)
        for seat in seats:
            seats_num[seat] += 1
        for student in students:
            students_num[student] += 1
        num = 0
        i = j = 1
        while i < len(students_num):
            if students_num[i]:
                while j < len(seats_num) and not seats_num[j]:
                    j += 1
                num += abs(i - j)
                seats_num[j] -= 1
                students_num[i] -= 1
            else:
                i += 1
        return num
