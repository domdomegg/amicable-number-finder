#!/usr/bin/env python3
# Amicable numbers
import math
import sys

if len(sys.argv) != 2:
	print("Usage: " + sys.argv[0] + " <maximum>")
	sys.exit()

def getDivisors(n):
	divisors = set()
	for i in range(1, int(math.ceil(math.sqrt(n))) + 1):
		if n % i == 0:
			divisors.add(i)
			divisors.add(n/i)
	return divisors

number_divisor_sums = {}

for i in range(0, int(sys.argv[1])):
	# Get divisors
	divisors = getDivisors(i)

	# Get sum of divisors minus i
	sum_of_divisors = int(sum(divisors) - i)

	# Store sum of divisors lower than i
	number_divisor_sums[i] = sum_of_divisors

	# Check if we have a match
	if (sum_of_divisors < i and
		number_divisor_sums[sum_of_divisors] == i):
		print("Match found at " + str([i, sum_of_divisors]))