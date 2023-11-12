
# [−1, −3, 5, −4, 3, −6, 9, 2]


def get_subarray_sums(input, subarray_len):
    subarrays_sum = {}
    for i in range(len(input) - subarray_len + 1):
        sum_ = sum(input[i:i+subarray_len+1])
        sum_ = 0 if sum_ < 0 else sum_
        subarrays_sum[str(input[i:i+subarray_len+1])] = sum_
    return subarrays_sum

def max_subarray_sum(input):
	
    subarray_sum = {}
    limit = len(input)
    for subarray_len in range(2, limit - 1):
        subarrays_sum_ = get_subarray_sums(input, subarray_len)
        subarray_sum.update(subarrays_sum_)

    sorted_subarray_sum = sorted(subarray_sum.items(), key=lambda x: x[1], reverse=True)    
    return sorted_subarray_sum[0][1]

foo = max_subarray_sum( [-1, -3, 5, -4, 3, -6, 9, 2])
print(foo)



def max_subarray_sum_optimized(input):
    max_sum = float('-inf')
    current_sum = 0

    for num in input:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
input_array = [-1, -3, 5, -4, 3, -6, 9, 2]
result = max_subarray_sum_optimized(input_array)
print(result)