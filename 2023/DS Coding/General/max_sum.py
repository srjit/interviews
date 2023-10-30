
# Given a list get the max possible product of three numbers

def max_three(input):
	
	input = sorted(input)
	last = input[-1]
	last_three = input[-3:]
	first_two = input[:2]
	return max(last_three[0]*last_three[1]*last, first_two[0]*first_two[1]*last)

print(max_three([1, 3, 4, 5]))
print(max_three([-4, -2, 3, 5]))

print(max_three([-4, -3, -2, -1]))
