def calculate_bitwise_complement(num):
	all_ones,l_bit , t_num = 0,1,num
	while num != 0:
		num = num//2
		all_ones |= l_bit
		l_bit <<= 1

	#return all_ones
	return t_num ^ all_ones

print(calculate_bitwise_complement(10))

