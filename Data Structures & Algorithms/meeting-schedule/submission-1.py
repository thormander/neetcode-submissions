"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # sort it
        intervals.sort(key=lambda i : i.start) # sort by start

        # start from 1 as we need to compare to preivous
        for interval in range(1,len(intervals)):
            first_interval = intervals[interval - 1]
            second_interval = intervals[interval]

            if second_interval.start < first_interval.end:
                return False
        
        return True