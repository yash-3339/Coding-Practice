#https://leetcode.com/problems/car-fleet/
class Solution:
    class Solution:
        def carFleet(self, target, pos, speed):
            time = [float(target - p) / s for p, s in sorted(zip(pos, speed))]
            res = cur = 0
            for t in time[::-1]:
                if t > cur:
                    res += 1
                    cur = t
            return res
def carFleet(target, pos, speed):
    if not pos:  # Handle empty input case
        return 0

    def calculate_time(p, s):
        if not isinstance(p, (int, float)) or not isinstance(s, (int, float)):
            raise ValueError("Position and speed must be numbers")
        if p < 0 or s <= 0 or target < p:
            raise ValueError("Invalid input: position >= 0, speed > 0, target >= position")
        return (target - p) / s

    times = [calculate_time(p, s) for p, s in zip(pos, speed)]
    sorted_times = list(sorted(times, reverse=True))  # Sort in descending order

    fleets = max_time = 0
    for time in sorted_times:
        if time > max_time:
            fleets += 1
            max_time = time

    return fleets
