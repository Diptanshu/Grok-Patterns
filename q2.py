def find_single_numbers(nums):
	'''
	 xor b/w 2 nos:
	 2 ^ 7 = 5 (=> 2 (2) ^ 7(1+4+2) => remove 2)
	 3 ^ 6 =  5 (=> 3 (1+2) ^ 6(4+2) -> remove 2, add 1,4 => 5) 
	'''
	res = 0
	for x in nums: 
		res = res ^ x # find overlapping bits atleast 1+

	# Check for the rightmost for dividing into 2 groups
	r_bit = 1
	while (res & r_bit == 0):
		r_bit = r_bit << 1

	l_num, r_num = 0,0
	for number in nums:
		if (number & r_bit != 0):
			l_num = l_num ^ number
		else:
			r_num = r_num ^ number

	return [l_num, r_num]

def main():
    print('Single numbers are:' + str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))


main()






