pages_total = int(input())
pages_per_hour = int(input())
num_of_days = int(input())
total_hours_needed = pages_total // pages_per_hour
hours_per_day = total_hours_needed // num_of_days
print(hours_per_day)
