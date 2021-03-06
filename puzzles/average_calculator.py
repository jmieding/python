"""
Python 2.7.10

This program returns an average (arithmetic mean) given
user-provided numbers. It ignores high and low outliers.

"""

def average_no_high_low(nums):
  organize = sorted(nums)
  no_high_low = organize[1:-1]
  print sum(no_high_low)/len(no_high_low)

print "Insert numbers with a space between each: "
user_input = raw_input()
nums = map(float, user_input.split())

average_no_high_low(nums)