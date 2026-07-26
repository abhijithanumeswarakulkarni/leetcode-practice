class Solution:
    def dayOfYear(self, date: str) -> int:
        # Brute Force - Time = O(n), space = O(1)
        date_split = date.split('-')
        year, month, day = int(date_split[0]), int(date_split[1]), int(date_split[2])
        total_days = 0
        for curr_month in range(1, month):
            if curr_month in [1, 3, 5, 7, 8, 10, 12]:
                total_days += 31
            elif curr_month in [4, 6, 9, 11]:
                total_days += 30
            else:
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    total_days += 29
                else:
                    total_days += 28
        total_days += day
        return total_days